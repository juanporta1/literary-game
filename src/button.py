import pygame
import src.const as const
import src.functions as functions

class Button:
    
    def __init__(self, x, y, width, height, text, font, primary_color, focus_color,text_color, value, screen):
        
        self.screen = screen
        self.font = font
        self.shape = pygame.Rect(x,y,width,height)
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
        self.screen.blit(self.text, (self.shape.left + ((self.shape.width - self.text.get_width()) / 2), self.shape.height / 3 + self.shape.top))
        

        
        
        