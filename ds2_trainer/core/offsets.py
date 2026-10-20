"""Static offsets for DS2.exe build 1.0.4.2 (2026-02-11)."""

OFFSETS = {
    "chiral_bandwidth": 0x0A1F2C40,
    "cargo_weight":     0x0A1F2D18,
    "stamina":          0x0A1F2E90,
    "bb_stress":        0x0A1F3050,
    "vehicle_fuel":     0x0A1F31A8,
    "timefall_timer":   0x0A1F33C0,
    "player_pos_x":     0x0A1F3A00,
    "player_pos_y":     0x0A1F3A04,
    "player_pos_z":     0x0A1F3A08,
}

# Pattern used to re-scan when game updates shift the base module.
SIGNATURE_CHIRAL = b"\xF3\x0F\x11\x87\x40\x2C\x1F\x0A"
SIGNATURE_STAMINA = b"\xF3\x0F\x11\x8F\x90\x2E\x1F\x0A"