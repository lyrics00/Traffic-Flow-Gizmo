import pygame
import os

def background_setup(screen, flags, bpp):
    pygame.init()
    
    screen_info = pygame.display.Info()
    screen_width, screen_height = screen_info.current_w, screen_info.current_h
    screen = pygame.display.set_mode(screen, flags, bpp)

    img = pygame.image.load("./backgroundStopSigns.png").convert()
    img2 = pygame.image.load("./sliders.PNG").convert()
    imgrect = img.get_rect()
    os.environ['SDL_VIDEO_WINDOW_POS'] = f"{(screen_width - 1180) // 2},{(screen_height - 800) // 2}"
    screen_width, screen_height = screen.get_width(), screen.get_height()
    img_width, img_height = img.get_width(), img.get_height()

    img_x = (screen_width - img_width) // 2
    img_y = (screen_height - img_height) // 2

    clock = pygame.time.Clock()
    pygame.mouse.set_visible(0)
    pygame.display.set_caption('Gizmo')
    
    screen.blit(img, (0, 0))
    screen.blit(img2, (imgrect.width, 0))
    sliderrect = img2.get_rect()
    return screen, img, img2, sliderrect, clock
