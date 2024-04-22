import pygame
import math
from classes.road import Intersection, Road, Lane

class Car:
    def __init__ (self, imageFile, speed, intersection: Intersection, road: Road, lane_num: int):
        self.speed = speed
        self.image = imageFile
        self.intersection = intersection
        self.road = road
        self.lane = self.GetCarLane(lane_num)
        self.x = self.lane.x_position
        self.y = self.lane.y_position
        self.turning_rate = 2  # Turning rate in degrees per frame
        self.turning = False  # Flag to indicate if the car is currently turning
        self.thread = None
        self.angle = self.Direction()

    def Show(self, surface):
        rotated_image = pygame.transform.rotate(self.image, float(self.angle+90))  # Rotate the car image based on the angle
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
        # Check if the car is turning
        if self.turning:
            if self.lane.turn_direction == 'right':
                self.angle -= self.turning_rate  # Turn right by decreasing angle
            elif self.lane.turn_direction == 'left':
                self.angle += self.turning_rate  # Turn left by increasing angle

            # Limit the angle within 0 to 360 degrees
            self.angle %= 360

        # Set the initial angle based on road orientation if not turning
        else:
            if self.road.orientation == "down":
                self.angle = 270
            elif self.road.orientation == "up":
                self.angle = 90
            elif self.road.orientation == "right":
                self.angle = 0
            elif self.road.orientation == "left":
                self.angle = 180
            else:
                self.angle = 0

        return self.angle
# Car thread method outside of car class
