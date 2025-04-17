# brittani chandler
# 4/2/2025
# settings.py
from pathlib import Path

class Settings:
    """Class to store all settings for Alien Invasion."""

    def __init__(self) -> None:
        """Initialize the game's settings."""
        self.ship_limit = 3

        self.screen_w = 1200
        self.screen_h = 800
        self.bg_color = (230, 230, 230)
        self.bg_file = Path.cwd() / 'images' / 'Starbasesnow.png'
        self.name = "Alien Invasion"

        self.ship_speed = 1.5
        self.ship_file = 'ship.png'

        # Bullet and sound settings
        self.bullet_file = Path.cwd() / 'images' / 'laserBlast.png'
        self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'laser.mp3'
        self.bullet_speed = 7
        self.bullet_w = 80
        self.bullet_h = 25
        self.bullet_amount = 5

        self.FPS = 60
        
        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1  # 1 = right, -1 = left
        
        # Game speed-up
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Settings that change as game progresses."""
        self.ship_speed = 1.5
        self.bullet_speed = 2.5
        self.alien_speed = 1.0
        self.fleet_direction = 1  # 1 = right, -1 = left
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)





