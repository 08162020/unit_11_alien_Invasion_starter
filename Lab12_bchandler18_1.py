"""alien invasion
Brittani Chandler
4/01/2025
"""

import sys
import pygame
from settings import Settings
from ship import Ship
from arsenal import Arsenal

class AlienInvasion:
    """Class to manage game initialization, resources, and the main game loop."""

    def __init__(self) -> None:
        """Initialize the game and create settings, screen, ship, and clock."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_w, self.settings.screen_h)
        )
        pygame.display.set_caption(self.settings.name)

        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(
            self.bg, (self.settings.screen_w, self.settings.screen_h)
        )

        self.clock = pygame.time.Clock()

        # Load sound
        self.laser_sound = pygame.mixer.Sound(self.settings.laser_sound)
        self.laser_sound.set_volume(0.7)

        # Create ship and assign arsenal
        self.ship = Ship(self)
        self.arsenal = Arsenal(self)

    def run_game(self) -> None:
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self.arsenal.update()

            self.screen.blit(self.bg, (0, 0))
            self.ship.blitme()
            self.arsenal.draw()
            pygame.display.flip()


    def _check_events(self) -> None:
        """Respond to keypresses and other events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event: pygame.event.Event) -> None:
        """Respond to keypresses."""
        # Only handle up/down and quit keys
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self.arsenal.fire_bullet()
            self.laser_sound.play()
            

    def _check_keyup_events(self, event: pygame.event.Event) -> None:
        """Respond to key releases."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

if __name__ == "__main__":
    ai_game = AlienInvasion()
    ai_game.run_game()



