import pygame
from background.background_gizmo import background_setup
from classes.car import Car
from classes.road import Intersection, Road, Lane
import os
import sys
from pygame.sprite import Sprite, Group
import random
pygame.init()
from pygame.locals import *
flags = DOUBLEBUF
screen, img, clock = background_setup((1150,820), flags, 16)
screen.set_alpha(None)
cimg1 = pygame.image.load("car1.png").convert_alpha()
cimg1rect = cimg1.get_rect()
cimg2 = pygame.image.load("car2.png").convert_alpha()
cimg2rect = cimg1.get_rect()
speed = 1.5
'''
    initialize()
    theoretically, we want a function that will initialize the screen with the background and the roads.
'''
# Your main game logic goes here
# For example:
def run_game(screen, bg, clock):
    pygame.mouse.set_visible(0)
    pygame.display.set_caption('Gizmo')# fix indentation
    #lane width is 120 pixels
    # def __init__(self, num_lanes: int, lane_height: int, lane_width: int, road_x_position: int, road_y_position: int, lane_directions: list[str], orientation: str):
    road1 = Road(num_lanes=3, lane_height=100, lane_width=120, road_x_position=315, road_y_position=-250, lane_directions=["straight", "straight", "straight"], orientation="down")
    road2 = Road(num_lanes=2, lane_height=120, lane_width=100, road_x_position=1000, road_y_position=-400, lane_directions=["straight", "straight", "straight"], orientation="left")
    # Assuming road1.lanes is a Group containing Lane sprites
    intersection1 = Intersection()
    intersection1.add_road(road1)
    intersection1.add_road(road2)
    # Get a list of Lane sprites from the Group
# Check if there are any Lane sprites in the list
    # def __init__ (self, imageFile, x, y, speed, intersection: Intersection, road: Road, lane_num: int):
    cars = []
    c1 = Car(cimg1, speed=speed, intersection=intersection1, road=road1, lane_num=0)
    cars.append(c1)
    c2 = Car(cimg2, speed=speed, intersection=intersection1, road=road1, lane_num=1)
    cars.append(c2)
    # Start all car threads

    # Join all car threads to wait for them to finish
    #first_lane.draw_border(screen)
    #second_lane.draw_border(screen)
    # Now you can use first_lane in your Car initialization
    while True:
        pygame.display.update()
        clock.tick(60)
        screen.blit(bg, (0, 0))
        c1.Show(screen)  
        c2.Show(screen)
        c1.Move()
        c2.Move()
        cars = DeleteCars(cars)
        '''
        update()
        Theoretically, we should just have a update function in the loop that organizes everything we want to update during each frame.
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    sys.exit()   
            pygame.display.update(cimg1rect)
            pygame.display.update(cimg2rect)
def update(list: list[Car]):
     #This method should import random to have a certain probability of a random car being generated and starts moving, should store a list of all the cars
     # list[cars] = GenerateCars(list)
     ''' for i in len(list):
            i.Move()
            i.Show(screen)
        cars = deleteCars(cars(a list))
        we should also have a method that deletes cars if they are out of the screen.
     '''
# TO DO: we should have a function that creates a car on the lane we want with a probabilistic image.
def CreateCar(imageFile, speed, intersection: Intersection, road: Road, lane_num: int):
    image = pygame.image.load(imageFile).convert_alpha()
    newCar = Car(image, speed, intersection, road, lane_num)
    return newCar
# TO DO: This method should import random to have a certain probability of a random car being generated and starts moving, should store a list of all the cars
def GenerateCars(list: list[Car]):
    num = random.random() * 100
    '''if num < 1:
        if num < 0.5:
            image = "car1.png" 
            list.append(CreateCar(image, speed, intersection, road, lane_num))
        else:
            image = "car2.png" 
            list.append(CreateCar(image,  speed, intersection, road, lane_num))
        '''
    return list
# TO DO: we should also have a method that deletes cars if they are out of the screen.
def DeleteCars(list: list[Car]):
    for car in list:
        [screen_x, screen_y] = screen.get_size()
        if screen_x < car.x or 0 > car.x or car.y > screen_y or car.y < 0:
            list.remove(car)
    return list
    




run_game(screen, img, clock)