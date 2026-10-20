"""Zero cargo weight / no encumbrance."""
from ds2_trainer.core.memory import MemoryBridge
from ds2_trainer.core.offsets import OFFSETS


class CargoWeight:
    def __init__(self, bridge: MemoryBridge):
        self.bridge = bridge
        self.zero = False

    def toggle(self) -> bool:
        self.zero = not self.zero
        return self.zero

    def tick(self) -> None:
        if self.zero:
            self.bridge.write_float(OFFSETS["cargo_weight"], 0.0)