"""TOML profile loader for trainer configuration."""
import os
import tomli

DEFAULT_PATH = os.path.join(os.path.dirname(__file__), "profiles")


def load_profile(name: str = "default") -> dict:
    path = os.path.join(DEFAULT_PATH, f"{name}.toml")
    with open(path, "rb") as fh:
        data = tomli.load(fh)
    return data