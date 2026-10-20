"""Pattern scanner used to re-locate offsets after game updates."""
from typing import Optional
import pymem


def scan_pattern(pm: pymem.Pymem, module_base: int, module_size: int, pattern: bytes) -> Optional[int]:
    data = pm.read_bytes(module_base, module_size)
    idx = data.find(pattern)
    if idx == -1:
        return None
    return module_base + idx