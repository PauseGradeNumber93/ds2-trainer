"""Infinite chiral bandwidth cheat."""
from ds2_trainer.core.memory import MemoryBridge
from ds2_trainer.core.offsets import OFFSETS

TARGET = 99999


class ChiralBandwidth:
    def __init__(self, bridge: MemoryBridge):
        self.bridge = bridge
        self._enabled = False

    def enable(self) -> None:
        if self._enabled:
            return
        self.bridge.write_float(OFFSETS["chiral_bandwidth"], float(TARGET))
        self._enabled = True

    def disable(self) -> None:
        if not self._enabled:
            return
        self.bridge.write_float(OFFSETS["chiral_bandwidth"], 0.0)
        self._enabled = False

    def tick(self) -> None:
        if self._enabled:
            current = self.bridge.read_float(OFFSETS["chiral_bandwidth"])
            if current < TARGET:
                self.bridge.write_float(OFFSETS["chiral_bandwidth"], float(TARGET))