# Brittani Chandler
# alien
# 4/8/2025


import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game: object, x: int = 0, y: int = 0) -> None:
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen: pygame.Surface = ai_game.screen
        self.settings = ai_game.settings

        # Load and scale the alien image to 40,40 pixels
        original_image = pygame.image.load('images/enemy_4.png')
        self.image: pygame.Surface = pygame.transform.scale(original_image, (40, 40))
        self.rect: pygame.Rect = self.image.get_rect()

        # Set the alien's starting position
        self.rect.x = x
        self.rect.y = y

        # Store precise horizontal position
        self.x: float = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at top or bottom edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.top <= 0 or self.rect.bottom >= screen_rect.bottom:
            return True


    def update(self) -> None:
        """Move the alien right or left."""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
