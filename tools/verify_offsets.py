"""Verify known offsets against a live DS2.exe instance."""
import sys
from ds2_trainer.core.memory import MemoryBridge
from ds2_trainer.core.offsets import OFFSETS
from ds2_trainer.config.loader import load_profile


def main() -> int:
    bridge = MemoryBridge("DS2.exe", load_profile("default"))
    if not bridge.attach():
        print("attach failed")
        return 1
    for name, off in OFFSETS.items():
        try:
            val = bridge.read_float(off)
            print(f"{name:20s} 0x{off:08x} -> {val:.3f}")
        except Exception as exc:
            print(f"{name:20s} FAILED: {exc}")
    bridge.detach()
    return 0


if __name__ == "__main__":
    sys.exit(main())