import pygame
class Car:
    def __init__ (self, imageFile, x, y, angle, speed):
        self.x = x
        self.y = y
        self.angle = 0
        self.speed = speed
        self.image = pygame.image.load(imageFile)
    def Show(self, surface):
        surface.blit(self.image, (self.x, self.y))
    def UpdateCoords(self, x):
        self.x = x