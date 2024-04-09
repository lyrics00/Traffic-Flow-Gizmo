import pygame
class Car:
    def __init__ (self, imageFile, x, y, angle, speed):
        self.x = x
        self.y = y
        self.angle = 0
        self.speed = speed
        self.image = pygame.image.load(imageFile)