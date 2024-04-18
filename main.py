import pygame
from background.background_gizmo import background_setup
from classes.car import Car
from classes.road import Intersection, Road, Lane
import os
import sys
pygame.init()
screen, bg, clock = background_setup(pygame.display.set_mode((1920, 1080)), "./background.png")
# Your main game logic goes here
# For example:
def run_game(screen, bg, clock):
    pygame.mouse.set_visible(0)
    pygame.display.set_caption('Gizmo')# fix indentation
    road1 = Road(3, 300, 100, 1000, 0, ["straight", "straight", "straight"], "up")
    # Assuming road1.lanes is a Group containing Lane sprites
    lane_sprites = road1.lanes.sprites()  # Get a list of Lane sprites from the Group

# Check if there are any Lane sprites in the list
    if len(lane_sprites) > 0:
    # Access the first Lane sprite from the list
        first_lane = lane_sprites[0]
    # Now you can use first_lane in your Car initialization
        c = Car("car1.png", road1.road_x_position, road1.road_y_position, 0, 4, road1, first_lane)
    else:
        print("No Lane sprites found in road1.lanes Group.")
    
    while True:
        clock.tick(60)
        screen.blit(bg, (0, 0))
        c.Show(screen)  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    sys.exit()    
            pygame.display.update()
run_game(screen, bg, clock)