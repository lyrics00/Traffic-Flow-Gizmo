import pygame
import math
from classes.road import Intersection, Road, Lane

class Car:
    def __init__ (self, imageFile, x, y, speed, intersection: Intersection, road: Road, lane: Lane):
        self.x = x
        self.y = y
        self.angle = 0
        self.speed = speed
        self.image = pygame.image.load(imageFile)
        self.intersection = intersection
        self.road = road
        self.lane = lane
        self.turning_rate = 2  # Turning rate in degrees per frame
        self.turning = False  # Flag to indicate if the car is currently turning

    def Show(self, surface):
        rotated_image = pygame.transform.rotate(self.image, self.angle)  # Rotate the car image based on the angle
        rect = rotated_image.get_rect(center=self.image.get_rect(topleft=(self.x, self.y)).center)  # Center the rotated image
        surface.blit(rotated_image, rect.topleft)  # Blit the rotated image onto the screen

    def UpdateCoords(self, x):
        self.x = x

    def Move(self):
        # Calculate the next position based on speed and direction
        next_x = self.x + self.speed * math.cos(math.radians(self.angle))
        next_y = self.y - self.speed * math.sin(math.radians(self.angle))  # Negative since y-coordinate increases downward in Pygame

        # Check if the next position is within the lane boundaries
        if self.lane.rect.collidepoint(next_x, next_y):
            self.x = next_x
            self.y = next_y
        else:
            self.StartTurning()  # Set turning flag to True when reaching the end of the lane

        # Gradually adjust the angle for turning
        if self.turning:
            if self.lane.turn_direction == 'right':
                self.angle -= self.turning_rate  # Turn right by decreasing angle
            elif self.lane.turn_direction == 'left':
                self.angle += self.turning_rate  # Turn left by increasing angle

            # Limit the angle within 0 to 360 degrees
            self.angle %= 360

            # Check if the turning is completed
            if abs(self.angle) % 90 == 0:  # Check if angle is a multiple of 90 degrees (indicating a completed turn)
                self.turning = False  # Set turning flag to False
                if self.lane.turn_direction == 'right':
                    self.lane = self.intersection.GetNextLane(self.lane, 'right')  # Get the next lane to the right
                elif self.lane.turn_direction == 'left':
                    self.lane = self.intersection.GetNextLane(self.lane, 'left')  # Get the next lane to the left

        # Adjust the car's coordinates to stay within the lane
        if not self.lane.rect.collidepoint(self.x, self.y):
            # If the car is outside the lane boundaries, move it back inside
            self.x -= self.speed * math.cos(math.radians(self.angle))
            self.y += self.speed * math.sin(math.radians(self.angle))

    def StartTurning(self):
        self.turning = True
