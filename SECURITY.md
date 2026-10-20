# Security Policy

## Scope

This repository is a hobbyist trainer for **Death Stranding 2: On the Beach**.
It performs read/write operations on the local game process via `pymem`.
It does not touch network traffic, does not phone home, and does not
distribute game binaries.

## Reporting

If you find a bug that could corrupt save data (e.g. a bad offset write
that persists into the save file), please open a private security advisory
on GitHub or email the maintainers listed in `pyproject.toml`.

## Warnings

- Use offline only. Using this trainer in online / shared worlds may violate
  Kojima Productions / Sony terms of service and can get your account banned.
- Never run the trainer alongside anti-cheat protected processes.
- Back up your save folder before enabling experimental features.
- Educational / modding purposes only. Use at your own risk.