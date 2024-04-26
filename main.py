import pygame
from src.player import Player

pygame.init()
screen = pygame.display.set_mode((1366,728),pygame.FULLSCREEN)
run = True

while run:
    pressed_keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if pressed_keys[pygame.K_ESCAPE]:
            run = False



pygame.quit()