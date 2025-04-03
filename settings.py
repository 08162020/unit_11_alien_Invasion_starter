# brittani chandler
# 4/2/2025
# settings.py
from pathlib import Path

class Settings:
    """Class to store all settings for Alien Invasion."""

    def __init__(self) -> None:
        """Initialize the game's settings."""
        self.screen_w = 1200
        self.screen_h = 800
        self.bg_color = (230, 230, 230)
        self.bg_file = Path.cwd() / 'images' / 'Starbasesnow.png'
        self.name = "Alien Invasion"

        self.ship_speed = 1.5
        self.ship_file = 'ship.png'

        # 🔹 Bullet and sound settings
        self.bullet_file = Path.cwd() / 'images' / 'laserBlast.png'
        self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'laser.mp3'
        self.bullet_speed = 7
        self.bullet_w = 25
        self.bullet_h = 80
        self.bullet_amount = 5

        self.FPS = 60



