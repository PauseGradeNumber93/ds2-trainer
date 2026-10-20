# Offset Reference (DS2.exe 1.0.4.2)

All offsets are relative to the `DS2.exe` module base.

| Name              | Offset      | Type  |
|-------------------|-------------|-------|
| chiral_bandwidth  | 0x0A1F2C40  | float |
| cargo_weight      | 0x0A1F2D18  | float |
| stamina           | 0x0A1F2E90  | float |
| bb_stress         | 0x0A1F3050  | float |
| vehicle_fuel      | 0x0A1F31A8  | float |
| timefall_timer    | 0x0A1F33C0  | float |
| player_pos_x/y/z  | 0x0A1F3A00  | float |

Re-run `tools/offset_dumper.py` after any Kojima Productions patch.