import pygame
import src.const as const
class Player:
    
    def __init__(self,x,y):
        self.shape = pygame.Rect(x, y, const.PLAYER_WIDTH, const.PLAYER_HEIGHT)
        
    def draw(self,screen,color):
        pygame.draw.rect(screen,color,self.shape,width=1)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if pressed_keys[pygame.K_w]:
            self.shape.y -= const.PLAYER_VELOCITY
        if pressed_keys[pygame.K_s]:
            self.shape.y += const.PLAYER_VELOCITY
        if pressed_keys[pygame.K_a]:
            self.shape.x -= const.PLAYER_VELOCITY
        if pressed_keys[pygame.K_d]:
            self.shape.x += const.PLAYER_VELOCITY