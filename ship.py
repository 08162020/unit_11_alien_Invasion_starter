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

        self.image: Surface = pygame.image.load("images/ship.png")
        self.rect: Rect = self.image.get_rect()
        self.screen_rect: Rect = self.screen.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        self.y: float = float(self.rect.y)
        self.x: float = float(self.rect.x)

        # Movement flags
        self.moving_right: bool = False
        self.moving_left: bool = False
        self.moving_up: bool = False
        self.moving_down: bool = False

        # Arsenal will be assigned after ship is created
        self.arsenal = None

    def update(self) -> None:
        """Update the ship's position based on movement flags."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

    def draw(self) -> None:
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)





