"""Snapshot of player state read from DS2.exe."""
from dataclasses import dataclass

from ds2_trainer.core.memory import MemoryBridge
from ds2_trainer.core.offsets import OFFSETS


@dataclass
class PlayerState:
    stamina: float
    cargo_weight: float
    bb_stress: float
    chiral_bandwidth: float

    @classmethod
    def read(cls, bridge: MemoryBridge) -> "PlayerState":
        return cls(
            stamina=bridge.read_float(OFFSETS["stamina"]),
            cargo_weight=bridge.read_float(OFFSETS["cargo_weight"]),
            bb_stress=bridge.read_float(OFFSETS["bb_stress"]),
            chiral_bandwidth=bridge.read_float(OFFSETS["chiral_bandwidth"]),
        )