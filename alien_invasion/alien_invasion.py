"""
In Alien Invasion, the player controls the ship that appears at the bottom center of the screen. The player can move the ship
right and left using the arrow keys and shoot bullets using spacebar. When the game begind, a fleet of aliens fills the sky
and move across and down the screen. The player shoots and destroy the aliens. If the player shoots all the aliens, a new fleet appears
that moves faster than the previous fleet. If any alien hits the player's ship or reaches the bottom of the screen, the player loses
a ship. If the player looses three ships the game ends.
"""

import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    """Initialize game and create a screen object"""
    pygame.init()  # initializes background settings
    ai_settings=Settings()
    screen = pygame.display.set_mode((ai_settings.screen_height,ai_settings.screen_width))  # 1200 pixels width, 800 pixels high
    pygame.display.set_caption("Alien Invasion")

    #Make a ship
    ship=Ship(screen)

    # Start the main loop for the game
    while True:
        # Watch for keyboard and mouses events
        gf.check_events(ship)
        gf.update_screen(ai_settings,screen,ship)

run_game()