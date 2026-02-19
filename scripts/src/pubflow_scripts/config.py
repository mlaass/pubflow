from pathlib import Path

# Root of the monorepo (3 levels up from this file: src/pubflow_scripts/config.py)
PROJECT_ROOT = Path(__file__).parents[3]

PIPELINE_ROOT = PROJECT_ROOT / "pipeline"
WEB_CONTENT_DIR = PROJECT_ROOT / "web" / "src" / "lib" / "content"
WEB_IMAGES_DIR = PROJECT_ROOT / "web" / "static" / "images"

STAGES = [
    "1_ideas",
    "2_research",
    "3_outlines",
    "4_drafts",
    "5_refined",
    "6_ready",
]
