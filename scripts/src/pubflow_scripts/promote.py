import re

import typer

from .config import PIPELINE_ROOT
from .utils import find_file, get_current_stage, get_next_stage

app = typer.Typer()

STAGE_NAMES = {
    "1_ideas": "ideas",
    "2_research": "research",
    "3_outlines": "outlines",
    "4_drafts": "drafts",
    "5_refined": "refined",
    "6_ready": "ready",
}


def update_frontmatter_stage(content: str, new_stage: str) -> str:
    """Update the stage field in frontmatter."""
    return re.sub(
        r"^(stage:\s*).*$",
        rf"\g<1>{new_stage}",
        content,
        count=1,
        flags=re.MULTILINE,
    )


@app.command()
def promote(id_prefix: str = typer.Argument(help="Content ID or numeric prefix (e.g. '002')")):
    """Move a content file from its current stage to the next."""
    file_path = find_file(id_prefix)
    if file_path is None:
        typer.echo(f"Error: No file found matching '{id_prefix}'", err=True)
        raise typer.Exit(code=1)

    current_stage = get_current_stage(file_path)
    if current_stage is None:
        typer.echo(f"Error: Could not determine stage for {file_path}", err=True)
        raise typer.Exit(code=1)

    next_stage = get_next_stage(current_stage)
    if next_stage is None:
        typer.echo(f"Error: '{file_path.name}' is already in the final stage ({current_stage})", err=True)
        raise typer.Exit(code=1)

    dest = PIPELINE_ROOT / next_stage / file_path.name
    dest.parent.mkdir(parents=True, exist_ok=True)

    # Update frontmatter stage field
    content = file_path.read_text()
    stage_name = STAGE_NAMES.get(next_stage, next_stage)
    content = update_frontmatter_stage(content, stage_name)
    dest.write_text(content)
    file_path.unlink()

    typer.echo(f"Promoted: {current_stage}/{file_path.name} → {next_stage}/{file_path.name}")
