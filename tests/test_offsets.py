from ds2_trainer.core.offsets import OFFSETS, SIGNATURE_CHIRAL


def test_offsets_are_positive():
    for name, off in OFFSETS.items():
        assert off > 0, name


def test_signature_length():
    assert len(SIGNATURE_CHIRAL) == 8