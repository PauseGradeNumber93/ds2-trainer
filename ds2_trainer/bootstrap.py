"""Entry point for the DS2 trainer overlay."""
import sys
import logging

from ds2_trainer.core.memory import MemoryBridge
from ds2_trainer.overlay.hud import TrainerHUD
from ds2_trainer.config.loader import load_profile

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(name)s :: %(message)s",
)


def main() -> int:
    profile = load_profile("default")
    bridge = MemoryBridge(process_name="DS2.exe", profile=profile)
    if not bridge.attach():
        logging.error("Could not attach to DS2.exe — is the game running?")
        return 1
    hud = TrainerHUD(bridge, profile)
    try:
        hud.run()
    finally:
        bridge.detach()
    return 0


if __name__ == "__main__":
    sys.exit(main())