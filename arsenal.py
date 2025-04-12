# brittani chandler
# arsenal file
# 4/2/2025


import pygame
from bullet import Bullet
from pygame.sprite import Group
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ship import Ship
    from Lab12_bchandler18_1 import AlienInvasion
    


class Arsenal:
    """A class to manage a group of bullets fired by the ship."""

    def __init__(self, ai_game: 'AlienInvasion') -> None:
        """
        Initialize the arsenal.

        Args:
            ai_game (AlienInvasion): The main game instance.
        """
        self.settings = ai_game.settings
        self.screen: pygame.Surface = ai_game.screen
        self.bullets: Group = pygame.sprite.Group()
        self.ship: 'Ship' = ai_game.ship  # Access the player's ship from the game

    def fire_bullet(self) -> None:
        """
        Fire a new bullet if below allowed limit.
        This method creates and adds a bullet to the bullets group.
        """
        if len(self.bullets) < self.settings.bullet_amount:
           new_bullet = Bullet(self.ship)
           new_bullet.rect.centery = self.ship.rect.centery
           new_bullet.rect.right = self.ship.rect.left
           new_bullet.x = float(new_bullet.rect.x)
           self.bullets.add(new_bullet)
    

    def update(self) -> None:
        """Update the position of bullets and remove any that go off-screen."""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.right < 0:
                self.bullets.remove(bullet)
    



    def draw(self) -> None:
        """Draw all active bullets to the screen."""
        for bullet in self.bullets.sprites():
            bullet.draw()

