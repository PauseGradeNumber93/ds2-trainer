# Architecture

```
ds2_trainer/
├── bootstrap.py       entry point
├── core/              memory bridge + offsets
├── features/          one cheat per module
├── models/            player state snapshots
├── overlay/           pygame HUD + hotkeys
├── config/            TOML profiles
├── services/          save backup
└── utils/             pattern scan, log helpers
```

The `MemoryBridge` owns the `pymem` handle. Feature modules receive
the bridge and read/write a fixed offset from `core/offsets.py`.
The HUD ticks all features at 30 Hz and renders their on/off state.