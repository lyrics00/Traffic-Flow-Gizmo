import pygame
from background.background_gizmo import background_setup
from classes.car import Car, car_thread
from classes.road import Intersection, Road, Lane
import os
import sys
from pygame.sprite import Sprite, Group
import threading
pygame.init()
screen, bg, clock = background_setup(pygame.display.set_mode((1920, 1080)), "./background.png")
'''
    initialize()
    theoretically, we want a function that will initialize the screen with the background and the roads.
'''
# Your main game logic goes here
# For example:
def run_game(screen, bg, clock):
    pygame.mouse.set_visible(0)
    pygame.display.set_caption('Gizmo')# fix indentation
    # def __init__(self, num_lanes: int, lane_height: int, lane_width: int, road_x_position: int, road_y_position: int, lane_directions: list[str], orientation: str):
    road1 = Road(num_lanes=3, lane_height=100, lane_width=120, road_x_position=200, road_y_position=-250, lane_directions=["straight", "straight", "straight"], orientation="up")
    # Assuming road1.lanes is a Group containing Lane sprites
    intersection1 = Intersection()
    intersection1.add_road(road1)
    # Get a list of Lane sprites from the Group
# Check if there are any Lane sprites in the list
    lanes = road1.getLanes()
    first_lane = lanes[0]
    second_lane = lanes[1]
    # def __init__ (self, imageFile, x, y, speed, intersection: Intersection, road: Road, lane_num: int):
    car_locks = [threading.Lock() for _ in range(2)]
    cars = []
    car_threads = []
    c1 = Car("car1.png", x=first_lane.x_position, y=first_lane.y_position, speed=1, intersection=intersection1, road=road1, lane_num=0)
    cars.append(c1)
    c2 = Car("car2.png", x=second_lane.x_position, y=second_lane.y_position, speed=1, intersection=intersection1, road=road1, lane_num=1)
    cars.append(c2)
    thread = threading.Thread(target=car_thread, args=(c1))
    car_threads.append(thread)
    thread = threading.Thread(target=car_thread, args=(c2))
    car_threads.append(thread)
    # Start all car threads
    for thread in car_threads:
        thread.start()
        thread.join()

    # Join all car threads to wait for them to finish
    #first_lane.draw_border(screen)
    #second_lane.draw_border(screen)
    # Now you can use first_lane in your Car initialization
      
    while True:
        clock.tick(15)
        screen.blit(bg, (0, 0))
        c1.Show(screen)  
        c2.Show(screen)
        '''
        update()
        Theoretically, we should just have a update function in the loop that organizes everything we want to update during each frame.
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    sys.exit()    
            pygame.display.update()
def update():
     #This method should import random to have a certain probability of a random car being generated and starts moving, should store a list of all the cars
     # list[cars] = GenerateCars(list)
     ''' for i in len(list[cars]):
            i.Move()
            i.Show(screen)
        list[cars] = deleteCars(list)
        we should also have a method that deletes cars if they are out of the screen.
     '''
# TO DO: we should have a function that creates a car on the lane we want with a probabilistic image.
def CreateCar():
    return
# TO DO: This method should import random to have a certain probability of a random car being generated and starts moving, should store a list of all the cars
def GenerateCars(list: list[Car]):
    return list
# TO DO: we should also have a method that deletes cars if they are out of the screen.
def DeleteCars(list: list[Car]):
    return list
    




run_game(screen, bg, clock)