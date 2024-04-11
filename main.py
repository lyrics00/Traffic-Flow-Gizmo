import pygame
from background.background_gizmo import background_setup
from classes.car import Car
import os
import sys
pygame.init()
screen, bg, clock = background_setup(pygame.display.set_mode((600, 480)), "./background.png")
# Your main game logic goes here
# For example:
def run_game(screen, bg, clock):
    pygame.mouse.set_visible(0)
    pygame.display.set_caption('Gizmo')# fix indentation
    c = Car("car1.png", 20, 20, 0, 4)
    while True:
        clock.tick(60)
        screen.blit(bg, (0, 0))
        x, y = pygame.mouse.get_pos()  
        c.UpdateCoords(x)
        c.Show(screen)  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    sys.exit()    
            pygame.display.update()
run_game(screen, bg, clock)