import pygame
import images
import src.const
import src.functions as functions
from src.functions import scale_ubication_y,scale_ubication_x
class Ladder:
    
    def __init__(self, x, y, image):
         self.image = functions.scale_images_screen(image)
         self.shape = pygame.Rect(scale_ubication_x(x), scale_ubication_y(y), image.get_width(), image.get_height())
         
    def draw(self, screen):
        screen.blit(self.image, self.shape)
    
    