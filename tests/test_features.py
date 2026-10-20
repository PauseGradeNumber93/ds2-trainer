from unittest.mock import MagicMock
from ds2_trainer.features.chiral_bandwidth import ChiralBandwidth
from ds2_trainer.features.stamina import Stamina


def test_chiral_enable_writes_target():
    bridge = MagicMock()
    feat = ChiralBandwidth(bridge)
    feat.enable()
    bridge.write_float.assert_called_once()


def test_stamina_lock_sets_flag():
    bridge = MagicMock()
    feat = Stamina(bridge)
    feat.lock()
    assert feat.locked is True
    feat.tick()
    bridge.write_float.assert_called()