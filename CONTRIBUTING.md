# Contributing to ds2-trainer

Thanks for helping improve the Death Stranding 2: On the Beach Trainer.

## Development setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Adding a new feature module

1. Drop a module under `ds2_trainer/features/`.
2. Register it in `ds2_trainer/overlay/hud.py`.
3. Add a hotkey entry to `ds2_trainer/config/profiles/default.toml`.
4. Write a test in `tests/` using `MagicMock` for the memory bridge.

## Updating offsets after a game patch

Run `python tools/offset_dumper.py` against a running DS2.exe to recover
the new addresses, then update `ds2_trainer/core/offsets.py`.

## Code style

- Python 3.11+, type hints where practical.
- Keep feature modules focused — one cheat per file.
- No blocking calls inside the HUD loop.