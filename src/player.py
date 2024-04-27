import pygame
import src.const as const
class Player:
    
    def __init__(self,x,y):
        self.shape = pygame.Rect(x, y, const.PLAYER_WIDTH, const.PLAYER_HEIGHT)
        
    def draw(self,screen,color):
        pygame.draw.rect(screen,color,self.shape,width=1)
        

       
    def move(self,stay_floor,is_first_floor,stay_ladder):
        pressed_keys = pygame.key.get_pressed()
        
        if pressed_keys[pygame.K_w] and stay_ladder:
            self.shape.y -= const.PLAYER_VELOCITY
        if pressed_keys[pygame.K_s] and not is_first_floor and stay_ladder:
            self.shape.y += const.PLAYER_VELOCITY
        if pressed_keys[pygame.K_a] and self.shape.left >= 0:
            self.shape.x -= const.PLAYER_VELOCITY
        if pressed_keys[pygame.K_d] and self.shape.right <= 1920:
            self.shape.x += const.PLAYER_VELOCITY
        if not stay_floor and not stay_ladder:
            self.shape.y += const.PLAYER_VELOCITY