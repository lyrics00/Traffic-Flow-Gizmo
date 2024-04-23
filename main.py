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
#  actual resolution is (1180, 800)
screen, bg, img_x, img_y, clock = background_setup((1180, 800), flags, 16)
screen.set_alpha(None)
cimg1 = pygame.image.load("car1.png").convert()
cimg1rect = cimg1.get_rect()
cimg2 = pygame.image.load("car2.png").convert()
cimg2rect = cimg1.get_rect()
SPEED = 1.5
FPS = 60
'''
    initialize()
    theoretically, we want a function that will initialize the screen with the background and the roads.
'''
# Your main game logic goes here
# For example
def run_game(screen, bg, img_x, img_y, clock):
    pygame.mouse.set_visible(0)
    pygame.display.set_caption('Gizmo')# fix indentation
    #lane width is 120 pixels
    # def __init__(self, num_lanes: int, lane_height: int, lane_width: int, road_x_position: int, road_y_position: int, lane_directions: list[str], orientation: str):
    road1 = Road(num_lanes=3, lane_height=100, lane_width=110, road_x_position=470, road_y_position=-250, lane_directions=["straight", "straight", "straight"], orientation="down", restriction_time= 1000.0)
    road2 = Road(num_lanes=1, lane_height=100, lane_width=110, road_x_position=1050, road_y_position=310, lane_directions=["straight"], orientation="left", restriction_time= 2000.0)
    road3 = Road(num_lanes=3, lane_height=100, lane_width=100, road_x_position=630, road_y_position=800, lane_directions=["straight", "straight", "straight"], orientation="up", restriction_time= 1000.0)
    road4 = Road(num_lanes=1, lane_height=100, lane_width=100, road_x_position=-300, road_y_position=400, lane_directions=["straight"], orientation="right", restriction_time= 2000.0)
    # Assuming road1.lanes is a Group containing Lane sprites
    intersection1 = Intersection()
    intersection1.add_road(road1)
    intersection1.add_road(road2)
    intersection1.add_road(road3)
    intersection1.add_road(road4)  
    # Get a list of Lane sprites from the Group
# Check if there are any Lane sprites in the list
    # def __init__ (self, imageFile, x, y, speed, intersection: Intersection, road: Road, lane_num: int):
    cars = pygame.sprite.Group()
    c1 = Car(cimg1, speed=SPEED, intersection=intersection1, road=road1, lane_num=0)
    cars.add(c1)
    c2 = Car(cimg2, speed=SPEED, intersection=intersection1, road=road2, lane_num=0)
    cars.add(c2)
    c3 = Car(cimg1, speed=SPEED, intersection=intersection1, road=road3, lane_num=0)
    cars.add(c3)
    c4 = Car(cimg2, speed=SPEED, intersection=intersection1, road=road4, lane_num=0)
    cars.add(c4)
    # Start all car threads

    # Join all car threads to wait for them to finish
    #first_lane.draw_border(screen)
    #second_lane.draw_border(screen)
    # Now you can use first_lane in your Car initialization
    while True:
        pygame.display.update()
        clock.tick(60)
        screen.blit(bg, (img_x, img_y))
        '''
        c1.Show(screen)  
        c2.Show(screen)
        c3.Show(screen)
        c4.Show(screen)
        c1.Move()
        c2.Move()
        c3.Move()
        c4.Move()
        update()
        Theoretically, we should just have a update function in the loop that organizes everything we want to update during each frame.
        '''
        update(cars, intersection1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.update(cimg1rect)
            pygame.display.update(cimg2rect)
def update(list: list[Car], intersection: Intersection):
     #This method should import random to have a certain probability of a random car being generated and starts moving, should store a list of all the cars
    list= GenerateCars(list, intersection=intersection)

    for i in list:
            car = i
            list.remove(i)
            i.kill
            list.add(car)

            i.Move()
            i.ShowScreen(screen, i.image)
    list = DeleteCars(list)
        #we should also have a method that deletes cars if they are out of the screen.
# TO DO: we should have a function that creates a car on the lane we want with a probabilistic image.
def CreateCar(imageFile, speed, intersection: Intersection, road: Road, lane_num: int):
    image = pygame.image.load(imageFile).convert_alpha()
    newCar = Car(image, speed, intersection, road, lane_num)
    return newCar
# TO DO: This method should import random to have a certain probability of a random car being generated and starts moving, should store a list of all the cars
def GenerateCars(list: list[Car], intersection: Intersection):
    num = random.random() * 8000
    if num < 100:
        if num < 50:
            image = "car1.png" 
        else:
            image = "car2.png" 
        rand_road = random.choice(intersection.roads)
        lane_num = random.randint(0, rand_road.num_lanes - 1)
        newCar = CreateCar(image, SPEED, intersection, rand_road, lane_num)
        collided_sprites = pygame.sprite.spritecollide(newCar, list, False)
        if len(collided_sprites) != 0:
            print("Collision Detected!")
            for car in collided_sprites:
                print(car.rect)
            newCar.kill()
        else:
            list.add(newCar)
    return list
# TO DO: we should also have a method that deletes cars if they are out of the screen.
def DeleteCars(list: list[Car]):
    for car in list:
        [screen_x, screen_y] = screen.get_size()
        if screen_x + 500 < car.x or -500 > car.x or car.y > screen_y + 500 or car.y < -500:
            list.remove(car)
            car.kill()
    return list
    




run_game(screen, bg, img_x, img_y, clock)