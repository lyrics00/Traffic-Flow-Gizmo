import pygame

def background_setup(screen, flags, bpp):
    pygame.init()
    
    screen = pygame.display.set_mode(screen, flags, bpp)
    img = pygame.image.load("./background.png").convert()
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(0)
    pygame.display.set_caption('Gizmo')

    return screen, img, clock