import pygame
import math
from classes.road import Intersection, Road, Lane

class Car:
    def __init__ (self, imageFile, x, y, speed, intersection: Intersection, road: Road, lane_num: int):
        self.x = x
        self.y = y
        self.speed = speed
        self.image = pygame.image.load(imageFile)
        self.intersection = intersection
        self.road = road
        self.lane = self.GetCarLane(lane_num)
        self.turning_rate = 2  # Turning rate in degrees per frame
        self.turning = False  # Flag to indicate if the car is currently turning
        self.thread = None
        self.angle = self.Direction()

    def Show(self, surface):
        rotated_image = pygame.transform.rotate(self.image, float(self.angle))  # Rotate the car image based on the angle
        rect = rotated_image.get_rect(center=self.image.get_rect(topleft=(self.x, self.y)).center)  # Center the rotated image
        surface.blit(rotated_image, rect.topleft)  # Blit the rotated image onto the screen

    def UpdateCoords(self, x,y):
        self.x = x
        self.y = y

    def Move(self):
        # Calculate the next position based on speed and direction
        next_x = self.x + self.speed * math.cos(math.radians(self.angle))
        next_y = self.y - self.speed * math.sin(math.radians(self.angle))  # Negative since y-coordinate increases downward in Pygame

        # Check if the next position is within the lane boundaries
    # if self.lane.collidepoint(next_x, next_y):
        self.x = next_x
        self.y = next_y
        #else:
        #   self.StartTurning()  # Set turning flag to True when reaching the end of the lane

        # Gradually adjust the angle for turning
        ''' if self.turning:
            if self.lane.turn_direction == 'right':
                self.angle -= self.turning_rate  # Turn right by decreasing angle
            elif self.lane.turn_direction == 'left':
                self.angle += self.turning_rate  # Turn left by increasing angle

            # Limit the angle within 0 to 360 degrees
            self.angle %= 360

            # Check if the turning is completed
            if abs(self.angle) % 90 == 0:  # Check if angle is a multiple of 90 degrees (indicating a completed turn)
                self.turning = False  # Set turning flag to False
                self.lane = self.GetNextLane(self.lane.turn_direction) 
        '''
        # Adjust the car's coordinates to stay within the lane
    #TO DO: when we turn with the car, we need to update the lane of the car correspondingly so we know how much to turn
    def GetNextLane(self, turn_direction):
        return self.lane
    def StartTurning(self):
        self.turning = True
    def GetCarLane(self, i):
        lane = self.road.getLanes()
        return lane[i]
    #TO DO: Turn based on current lane and next lane
    def Turn(self, next_lane):
        return
    
    #TO DO: stop depending on traffic.
    def Stop():
        return
    def Direction(self):
        if self.road.orientation == "down":
            angle = 270
        if self.road.orientation == "up":
            angle = 90
        if self.road.orientation == "right":
            angle = 0
        if self.road.orientation == "left":
            angle = 180
        else:
            angle = 0
        return angle

# Car thread method outside of car class

def car_thread(car):
    clock = pygame.time.Clock()
    while True:
        car.Move()
        clock.tick(15)  # Adjust as needed for desired framerate