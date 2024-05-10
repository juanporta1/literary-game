import pygame
import src.const as const
import src.functions as functions
from functions import scale_ubication_y,scale_ubication_x

class Button:
    
    def __init__(self, x, y, width, height, text, font, primary_color, focus_color,text_color, value, screen):
        
        self.screen = screen
        self.font = font
        self.shape = pygame.Rect(scale_ubication_x(x),scale_ubication_y(y),scale_ubication_x(width),scale_ubication_y(height))
        self.text = self.font.render(text,0,text_color)
        self.primary_color = primary_color
        self.focus_color = focus_color
        self.text_color = text_color
        self.value = value
        self.selected = False
        
    def draw(self):
        mx,my = pygame.mouse.get_pos()
        if self.selected:
            pygame.draw.rect(self.screen,self.focus_color,self.shape)
        else:
            pygame.draw.rect(self.screen,self.primary_color,self.shape)
        self.screen.blit(self.text, (scale_ubication_x(self.shape.left + ((self.shape.width - self.text.get_width()) / 2)), scale_ubication_y(self.shape.height / 3 + self.shape.top)))
        

        
        
        