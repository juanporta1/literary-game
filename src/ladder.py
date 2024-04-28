import pygame
import images
import src.const
import src.functions as functions
class Ladder:
    
    def __init__(self, x, y, image):
         self.image = functions.scale_images_screen(image)
         self.shape = pygame.Rect(x, y, image.get_width(), image.get_height())
         
    def draw(self, screen):
        screen.blit(self.image, self.shape)
    
    