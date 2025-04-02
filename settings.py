# settings.py
# Author: [Your Name]
# Description: Stores configuration settings for the Alien Invasion game.
# Date: April 1, 2025

class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self) -> None:
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width: int = 1200
        self.screen_height: int = 800
        self.bg_color: tuple[int, int, int] = (230, 230, 230)

        # Ship settings
        self.ship_speed: float = 1.5
