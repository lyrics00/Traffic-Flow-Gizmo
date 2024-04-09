import pygame # type: ignore
import sys
import os

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
    

# from pygame.locals import *pygame.init()  # initialize pygame
clock = pygame.time.Clock()
screen = pygame.display.set_mode((600, 480))# Load the background image here. Make sure the file exists!
bg = pygame.image.load(os.path.join("./", "background.png"))
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