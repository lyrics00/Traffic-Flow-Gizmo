import pygame
import os

def background_setup(screen, img_path):
    pygame.init()
    screen_info = pygame.display.Info()
    screen_width, screen_height = screen_info.current_w, screen_info.current_h

    screen = pygame.display.set_mode((1180, 800))
    os.environ['SDL_VIDEO_WINDOW_POS'] = f"{(screen_width - 1180) // 2},{(screen_height - 800) // 2}"

    bg = pygame.image.load(img_path)
    bg = pygame.transform.flip(bg, True, True)

    screen_width, screen_height = screen.get_width(), screen.get_height()
    bg_width, bg_height = bg.get_width(), bg.get_height()

    bg_x = (screen_width - bg_width) // 2
    bg_y = (screen_height - bg_height) // 2

    clock = pygame.time.Clock()
    pygame.mouse.set_visible(0)
    pygame.display.set_caption('Gizmo')

    screen.blit(bg, (bg_x, bg_y))

    return screen, bg, clock
