import re
from pathlib import Path

from .config import PIPELINE_ROOT, STAGES


def slugify(text: str) -> str:
    """Convert text to URL-friendly slug."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


def get_next_sequence() -> int:
    """Find the highest existing sequence number across all stages and return next."""
    max_seq = 0
    for stage in STAGES:
        stage_dir = PIPELINE_ROOT / stage
        if not stage_dir.exists():
            continue
        for f in stage_dir.iterdir():
            if f.suffix == ".md" and f.name != ".gitkeep":
                match = re.match(r"^(\d{3})-", f.name)
                if match:
                    max_seq = max(max_seq, int(match.group(1)))
    return max_seq + 1


def make_id(sequence: int, title: str) -> str:
    """Create a content ID like '002-my-topic'."""
    return f"{sequence:03d}-{slugify(title)}"


def find_file(id_prefix: str) -> Path | None:
    """Find a pipeline file by its numeric ID prefix (e.g. '002' or '002-my-topic').

    Searches all stages and returns the first match.
    """
    for stage in STAGES:
        stage_dir = PIPELINE_ROOT / stage
        if not stage_dir.exists():
            continue
        for f in stage_dir.iterdir():
            if f.suffix == ".md" and f.name.startswith(id_prefix.split("-")[0].zfill(3)):
                return f
    return None


def get_current_stage(file_path: Path) -> str | None:
    """Get the stage name from a file's parent directory."""
    parent = file_path.parent.name
    if parent in STAGES:
        return parent
    return None


def get_next_stage(current_stage: str) -> str | None:
    """Get the next stage after the given one."""
    try:
        idx = STAGES.index(current_stage)
        if idx + 1 < len(STAGES):
            return STAGES[idx + 1]
    except ValueError:
        pass
    return None
