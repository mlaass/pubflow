from datetime import date

import typer

from .config import PIPELINE_ROOT
from .utils import get_next_sequence, make_id

app = typer.Typer()


@app.command()
def new(title: str = typer.Argument(help="Title for the new content idea")):
    """Create a new content idea in the pipeline."""
    seq = get_next_sequence()
    content_id = make_id(seq, title)
    dest = PIPELINE_ROOT / "1_ideas" / f"{content_id}.md"

    dest.parent.mkdir(parents=True, exist_ok=True)

    frontmatter = f"""---
id: "{seq:03d}"
title: "{title}"
slug: {content_id}
created: {date.today().isoformat()}
tags: []
stage: ideas
---

# {title}

## Core Idea



## Angle



## Notes

"""
    dest.write_text(frontmatter)
    typer.echo(f"Created: pipeline/1_ideas/{content_id}.md")
