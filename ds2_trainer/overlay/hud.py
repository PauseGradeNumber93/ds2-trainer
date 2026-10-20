"""Pygame HUD overlay drawn on top of the DS2 window."""
import logging
import pygame
import keyboard

from ds2_trainer.core.memory import MemoryBridge
from ds2_trainer.features.chiral_bandwidth import ChiralBandwidth
from ds2_trainer.features.stamina import Stamina
from ds2_trainer.features.cargo_weight import CargoWeight
from ds2_trainer.features.bb_stress import BBStress
from ds2_trainer.features.timefall import TimefallControl

log = logging.getLogger(__name__)


class TrainerHUD:
    def __init__(self, bridge: MemoryBridge, profile: dict):
        self.bridge = bridge
        self.profile = profile
        self.features = {
            "chiral": ChiralBandwidth(bridge),
            "stamina": Stamina(bridge),
            "cargo": CargoWeight(bridge),
            "bb": BBStress(bridge),
            "timefall": TimefallControl(bridge),
        }
        self._bind_hotkeys()

    def _bind_hotkeys(self) -> None:
        keyboard.add_hotkey(self.profile["hotkeys"]["chiral"], self.features["chiral"].enable)
        keyboard.add_hotkey(self.profile["hotkeys"]["stamina"], self.features["stamina"].lock)
        keyboard.add_hotkey(self.profile["hotkeys"]["cargo"], self.features["cargo"].toggle)
        keyboard.add_hotkey(self.profile["hotkeys"]["bb"], self.features["bb"].freeze)
        keyboard.add_hotkey(self.profile["hotkeys"]["timefall"], self.features["timefall"].clear)

    def run(self) -> None:
        pygame.init()
        screen = pygame.display.set_mode((360, 220), pygame.NOFRAME)
        pygame.display.set_caption("DS2 Trainer")
        clock = pygame.time.Clock()
        font = pygame.font.SysFont("consolas", 14)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            for f in self.features.values():
                if hasattr(f, "tick"):
                    f.tick()
            screen.fill((12, 14, 20))
            y = 10
            for name, feat in self.features.items():
                active = getattr(feat, "_enabled", getattr(feat, "locked",
                         getattr(feat, "zero", getattr(feat, "frozen", False))))
                color = (60, 220, 140) if active else (150, 150, 150)
                screen.blit(font.render(f"{name:12s} : {'ON' if active else 'off'}", True, color), (12, y))
                y += 22
            pygame.display.flip()
            clock.tick(30)
        pygame.quit()