import pygame
import src.const
import src.functions as functions

class Floor:
    def __init__(self, image, x, y):
        self.image = functions.scale_images_screen(image)
        self.floor = pygame.Rect(x, y, self.image.get_width(), self.image.get_height())
        
    def draw(self, screen):
        screen.blit(self.image, self.floor)
