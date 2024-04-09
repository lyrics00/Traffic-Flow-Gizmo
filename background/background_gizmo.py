import pygame

def background_setup(screen, img_path):
    pygame.init()
    screen = pygame.display.set_mode((600, 480))
    bg = pygame.image.load(img_path)

    clock = pygame.time.Clock()
    pygame.mouse.set_visible(0)
    pygame.display.set_caption('Gizmo')

    return screen, bg, clock
