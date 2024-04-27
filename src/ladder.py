import pygame
import images
import src.const
import src.functions as functions
class Ladder:
    
    def __init__(self, x, y, image):
         self.image = functions.scale_images(image)
         self.shape = pygame.Rect(x, y, image.get_width(), image.get_height())
         
    def draw(self, screen):
        screen.blit(self.image, self.shape)
        pygame.draw.rect(rect=self.shape, surface=screen, color=(0,255,0), width=1)