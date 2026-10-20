"""Infinite vehicle fuel for reverse trike / truck."""
from ds2_trainer.core.memory import MemoryBridge
from ds2_trainer.core.offsets import OFFSETS

FULL = 100.0


class VehicleFuel:
    def __init__(self, bridge: MemoryBridge):
        self.bridge = bridge
        self.enabled = False

    def toggle(self) -> bool:
        self.enabled = not self.enabled
        return self.enabled

    def tick(self) -> None:
        if self.enabled:
            self.bridge.write_float(OFFSETS["vehicle_fuel"], FULL)