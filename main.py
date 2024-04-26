import pygame
from src.player import Player

pygame.init()
screen = pygame.display.set_mode((1366,728),pygame.FULLSCREEN)
run = True

player = Player(x = 100,
                y = 100)

clock = pygame.time.Clock()
FPS = 60

sky_bg = pygame.image.load("assets//proof_assets//sky_bg.png")
sky_bg = pygame.transform.scale(sky_bg, (sky_bg.get_width() * 6, sky_bg.get_height() * 4))

while run:
    clock.tick(FPS)
    screen.blit(sky_bg, (0,0))
    pressed_keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if pressed_keys[pygame.K_ESCAPE]:
            run = False

    player.draw(screen,(255,255,0))
    player.move()
    
    pygame.display.update()

pygame.quit()