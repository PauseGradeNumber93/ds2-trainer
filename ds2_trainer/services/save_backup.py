"""Backup DS2 save files before enabling risky features."""
import os
import shutil
import time
from pathlib import Path

SAVE_ROOT = Path(os.environ.get("USERPROFILE", ".")) / "Documents" / "KojimaProductions" / "DS2"


def backup(dest: Path = Path("./backups")) -> Path:
    dest.mkdir(parents=True, exist_ok=True)
    stamp = time.strftime("%Y%m%d_%H%M%S")
    target = dest / f"ds2_save_{stamp}"
    if SAVE_ROOT.exists():
        shutil.copytree(SAVE_ROOT, target)
    return target