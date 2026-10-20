"""BB stress / odradek meter freeze."""
from ds2_trainer.core.memory import MemoryBridge
from ds2_trainer.core.offsets import OFFSETS

CALM = 0.0


class BBStress:
    def __init__(self, bridge: MemoryBridge):
        self.bridge = bridge
        self.frozen = False

    def freeze(self) -> None:
        self.frozen = True

    def unfreeze(self) -> None:
        self.frozen = False

    def tick(self) -> None:
        if self.frozen:
            self.bridge.write_float(OFFSETS["bb_stress"], CALM)