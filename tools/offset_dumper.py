"""Standalone offset dumper — scans DS2.exe for known signatures."""
import sys
import pymem
import pymem.process

from ds2_trainer.core.offsets import SIGNATURE_CHIRAL, SIGNATURE_STAMINA
from ds2_trainer.utils.scan import scan_pattern


def main() -> int:
    try:
        pm = pymem.Pymem("DS2.exe")
    except pymem.exception.ProcessNotFound:
        print("DS2.exe not running")
        return 1
    mod = pymem.process.module_from_name(pm.process_handle, "DS2.exe")
    if mod is None:
        print("module not found")
        return 1
    for name, sig in (("chiral", SIGNATURE_CHIRAL), ("stamina", SIGNATURE_STAMINA)):
        addr = scan_pattern(pm, mod.lpBaseOfDll, mod.SizeOfImage, sig)
        print(f"{name:10s} -> {hex(addr) if addr else 'not found'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())