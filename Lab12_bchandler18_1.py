"""alien invasion
Brittani Chandler
4/01/2025
"""

import sys
import pygame
from settings import Settings
from ship import Ship
from arsenal import Arsenal
from alien import Alien

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
        
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
    def run_game(self) -> None:
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self.arsenal.update()
            self._check_bullet_alien_collisions()
            self._update_aliens()
            self.screen.blit(self.bg, (0, 0))
            self.ship.blitme()
            self.arsenal.draw()
            self.aliens.draw(self.screen)
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
    
    
    def _update_aliens(self) -> None:
        """Update aliens and respond to edge collisions."""
        self._check_fleet_edges()
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        for alien in self.aliens.sprites():
            if alien.rect.right >= self.settings.screen_w:
                self._ship_hit()
                break


    # Check for alien hitting right edge
        for alien in self.aliens.sprites():
            if alien.rect.right >= self.settings.screen_w:
                self._ship_hit()
                break

    def _check_fleet_edges(self) -> None:
        """Drop the fleet and reverse direction if any alien hits screen edge."""
        for alien in self.aliens.sprites():
            if alien.rect.right >= self.settings.screen_w or alien.rect.left <= 0:
                for a in self.aliens.sprites():
                    a.rect.y += self.settings.fleet_drop_speed
                self.settings.fleet_direction *= -1
                print(f"Fleet direction changed to {self.settings.fleet_direction}")

                break


    def _change_fleet_direction(self) -> None:  
        """Drop the fleet and reverse direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _create_fleet(self):
        """Create a vertical fleet of aliens spaced along the horizontal axis."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        max_columns = 5
        column_count = 0
        current_x = alien_width

        while column_count < max_columns:
            current_y = alien_height
            while current_y < (self.settings.screen_h - 3 * alien_height):
                self._create_alien(current_x, current_y)
                current_y += 2.5 * alien_height  
            current_x += 2.5 * alien_width     
            column_count += 1

    def _create_alien(self, x: int, y: int) -> None:  
        """Create one alien and add it to the fleet."""
        alien = Alien(self, x, y)
        self.aliens.add(alien)
        
    def _check_bullet_alien_collisions(self):
        """Check for any bullets that have hit aliens, and remove both."""
        collisions = pygame.sprite.groupcollide(
        self.arsenal.bullets, self.aliens, True, True)

    def _ship_hit(self):
        """Reset the game when the ship is hit or aliens reach the edge."""
        print("Ship hit or edge reached — resetting game!")

    # Clear all bullets and aliens
        self.aliens.empty()
        self.arsenal.bullets.empty()

    # Re-center the ship
        self.ship.rect.midright = self.screen.get_rect().midright
        self.ship.y = float(self.ship.rect.y)

    # Rebuild the fleet
        self._create_fleet()


if __name__ == "__main__":
    ai_game = AlienInvasion()
    ai_game.run_game()



