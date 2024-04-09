import pygame
from background.background_gizmo import background_setup
import os
import sys
pygame.init()
screen, bg, clock = background_setup(pygame.display.set_mode((600, 480)), "./background.png")
# Your main game logic goes here
# For example:
def run_game(screen, bg, clock):
    pygame.mouse.set_visible(0)
    pygame.display.set_caption('Gizmo')
    while True:
        clock.tick(60)
        screen.blit(img, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Exit the background loop if the window is closed
        pygame.display.update()
run_game(screen, bg, clock)