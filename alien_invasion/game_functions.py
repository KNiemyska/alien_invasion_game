import sys
import pygame
def check_events(ship):
    """Respond to keypress and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                #Move ship to right
                ship.rect.centerx+=1
def update_screen(ai_settings,screen,ship):
    # Redraw the screen during each pass through the loop
    screen.fill(ai_settings.bg_color)
    ship.bltime()
    # Make the most recently drawn screen visable
    pygame.display.flip()
