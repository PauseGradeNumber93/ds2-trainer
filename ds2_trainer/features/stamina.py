"""Stamina freeze / infinite stamina for DS2."""
from ds2_trainer.core.memory import MemoryBridge
from ds2_trainer.core.offsets import OFFSETS

MAX_STAMINA = 100.0


class Stamina:
    def __init__(self, bridge: MemoryBridge):
        self.bridge = bridge
        self.locked = False

    def lock(self) -> None:
        self.locked = True

    def unlock(self) -> None:
        self.locked = False

    def tick(self) -> None:
        if self.locked:
            self.bridge.write_float(OFFSETS["stamina"], MAX_STAMINA)