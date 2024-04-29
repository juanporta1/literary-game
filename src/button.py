import pygame
import src.const as const
import src.functions as functions

class Button:
    
    
    
    def __init__(self, x, y, width, height, text, font, primary_color, focus_color,text_color, value, screen):
        
        self.screen = screen
        self.font = pygame.font.Font(font, 30)
        self.shape = pygame.Rect(x,y,width,height)
        self.text = self.font.render(text,0,text_color)
        self.primary_color = primary_color
        self.focus_color = focus_color
        self.text_color = text_color
        self.value = value
        
    def draw(self):
        mx,my = pygame.mouse.get_pos()
        if self.shape.collidepoint(mx,my):
            pygame.draw.rect(self.screen,self.focus_color,self.shape)
        else:
            pygame.draw.rect(self.screen,self.primary_color,self.shape)
        self.screen.lit(self.text, (self.shape.width / 4 + self.shape.left, self.shape.height / 4 + self.shape.top))
        
        