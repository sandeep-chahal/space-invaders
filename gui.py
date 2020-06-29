import pygame
from os import path
pygame.font.init()

classic_font = pygame.font.Font(path.join("assets", "ARCADECLASSIC.TTF"), 25)


def show_level(screen, level):
    width = classic_font.size(f"Level {level}")[0]
    level_title = classic_font.render(f"Level {level}", 1, (255, 255, 255))
    screen.blit(level_title, (screen.get_width() - width-10, 10))
