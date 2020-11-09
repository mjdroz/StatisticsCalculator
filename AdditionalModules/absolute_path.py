from pathlib import Path

def absolute_path(filepath):
    relative_path = Path(filepath)
    return relative_path.absolute()