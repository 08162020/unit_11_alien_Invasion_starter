# Brittani Chandler
# Bullet file
# 4/2/2025


import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ship import Ship  # Only imported for type hints, avoids circular import

class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, ai_game: 'Ship') -> None:
        """
        Create a bullet object at the ship's current position.

        Args:
            ai_game (Ship): The ship instance to align bullet positioning.
        """
        super().__init__()
        self.screen: pygame.Surface = ai_game.screen
        self.settings = ai_game.settings

        # Load and scale the bullet image
        self.image: pygame.Surface = pygame.image.load(self.settings.bullet_file)
        self.image = pygame.transform.scale(
            self.image,
            (self.settings.bullet_w, self.settings.bullet_h)
        )

        self.rect: pygame.Rect = self.image.get_rect()
        self.rect.midtop = ai_game.rect.midtop

        self.y: float = float(self.rect.y)

    def update(self) -> None:
        """Move the bullet up the screen."""
        self.y -= self.settings.bullet_speed
        self.rect.y = int(self.y)

    def draw(self) -> None:
        """Draw the bullet on the screen."""
        self.screen.blit(self.image, self.rect)

