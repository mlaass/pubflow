import shutil

import typer

from .config import PIPELINE_ROOT, WEB_CONTENT_DIR, WEB_IMAGES_DIR
from .utils import find_file

app = typer.Typer()


@app.command()
def publish(id_prefix: str = typer.Argument(help="Content ID or numeric prefix (e.g. '002')")):
    """Copy a finished article from 6_ready/ to the web app's content directory."""
    file_path = find_file(id_prefix)
    if file_path is None:
        typer.echo(f"Error: No file found matching '{id_prefix}'", err=True)
        raise typer.Exit(code=1)

    if file_path.parent.name != "6_ready":
        typer.echo(
            f"Error: '{file_path.name}' is in {file_path.parent.name}, not 6_ready. "
            "Promote it to 6_ready first.",
            err=True,
        )
        raise typer.Exit(code=1)

    # Copy markdown to web content
    WEB_CONTENT_DIR.mkdir(parents=True, exist_ok=True)
    dest_md = WEB_CONTENT_DIR / file_path.name
    shutil.copy2(file_path, dest_md)
    typer.echo(f"Published: {file_path.name} → web/src/lib/content/")

    # Copy associated images if they exist
    images_dir = PIPELINE_ROOT / "6_ready" / "images" / file_path.stem
    if images_dir.exists():
        WEB_IMAGES_DIR.mkdir(parents=True, exist_ok=True)
        dest_images = WEB_IMAGES_DIR / file_path.stem
        if dest_images.exists():
            shutil.rmtree(dest_images)
        shutil.copytree(images_dir, dest_images)
        typer.echo(f"Published images: {images_dir.name}/ → web/static/images/")
