from __future__ import annotations
"""ship.py
Author: Brittani Chandler
Description: Defines the Ship class for the Alien Invasion game.
Handles image loading, movement, and collision rectangle setup.
Date: April 1, 2025
"""
import pygame
from pygame.surface import Surface
from pygame.rect import Rect


class Ship:
    """A class to manage the player's ship."""

    def __init__(self, game: AlienInvasion) -> None:
        """Initialize the ship and set its starting position."""
        self.screen: Surface = game.screen
        self.settings = game.settings

        # LOAD and ROTATE image to face right (toward center)
        original_image = pygame.image.load("images/ship.png")
        self.image: Surface = pygame.transform.rotate(original_image, -90)  # Face right

        self.rect: Rect = self.image.get_rect()
        self.screen_rect: Rect = self.screen.get_rect()

        # Position the ship on the LEFT side, vertically centered
        self.rect.left = self.screen_rect.left
        self.rect.centery = self.screen_rect.centery

        # Position values for smooth movement
        self.y: float = float(self.rect.y)

        # Movement flags: Only up and down
        self.moving_up: bool = False
        self.moving_down: bool = False

    def update(self) -> None:
        """Update the ship's position based on movement flags."""
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        self.rect.y = self.y

    def blitme(self) -> None:
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)






