"""Timefall timer manipulation."""
from ds2_trainer.core.memory import MemoryBridge
from ds2_trainer.core.offsets import OFFSETS


class TimefallControl:
    def __init__(self, bridge: MemoryBridge):
        self.bridge = bridge

    def clear(self) -> None:
        self.bridge.write_float(OFFSETS["timefall_timer"], 0.0)

    def set_timer(self, seconds: float) -> None:
        self.bridge.write_float(OFFSETS["timefall_timer"], seconds)