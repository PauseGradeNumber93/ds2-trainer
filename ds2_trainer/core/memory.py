"""Low-level memory read/write bridge for DS2.exe."""
import logging
from dataclasses import dataclass
from typing import Optional

import pymem
import pymem.process

log = logging.getLogger(__name__)


@dataclass
class ModuleBase:
    name: str
    address: int
    size: int


class MemoryBridge:
    def __init__(self, process_name: str, profile: dict):
        self.process_name = process_name
        self.profile = profile
        self.pm: Optional[pymem.Pymem] = None
        self.module: Optional[ModuleBase] = None

    def attach(self) -> bool:
        try:
            self.pm = pymem.Pymem(self.process_name)
        except pymem.exception.ProcessNotFound:
            log.warning("process %s not found", self.process_name)
            return False
        mod = pymem.process.module_from_name(
            self.pm.process_handle, self.profile["base_module"]
        )
        if mod is None:
            log.warning("base module %s missing", self.profile["base_module"])
            return False
        self.module = ModuleBase(mod.name, mod.lpBaseOfDll, mod.SizeOfImage)
        log.info("attached to %s @ 0x%x", mod.name, mod.lpBaseOfDll)
        return True

    def resolve(self, offset: int) -> int:
        assert self.module is not None, "attach() first"
        return self.module.address + offset

    def read_float(self, offset: int) -> float:
        assert self.pm is not None
        return self.pm.read_float(self.resolve(offset))

    def write_float(self, offset: int, value: float) -> None:
        assert self.pm is not None
        self.pm.write_float(self.resolve(offset), value)

    def read_int(self, offset: int) -> int:
        assert self.pm is not None
        return self.pm.read_int(self.resolve(offset))

    def write_int(self, offset: int, value: int) -> None:
        assert self.pm is not None
        self.pm.write_int(self.resolve(offset), value)

    def detach(self) -> None:
        if self.pm is not None:
            try:
                self.pm.close_process()
            except Exception:
                pass
            self.pm = None