from src.ladder import Ladder
import pygame
import random

class Ladders_Create:
    
    def __init__(self, x, y, quantity, image, screen):
        self.ladders= []
        self.initial_x = x
        self.initial_y = y
        self.actual_y= y
        self.quantity = quantity
        self.image = image
        self.screen = screen
        self.all_ladder = pygame.Rect(x, y -  (image.get_height() * quantity), image.get_width(), image.get_height() * quantity)
        self.create_all_ladder()
        
        
    def create_all_ladder(self):
        for i in range(self.quantity):
            
            individual_ladder = Ladder(image=self.image, x=self.initial_x, y=self.actual_y - self.image.get_height())
            self.ladders.append(individual_ladder)
            self.actual_y -= individual_ladder.shape.height    
        self.actual_y = self.initial_y

    def detect_ladder(ladders, player):
        stay_ladder = False
        
        for i in ladders:
            
            if player.shape.left <= i.all_ladder.right - 10 and player.shape.right >= i.all_ladder.left + 10 and player.shape.bottom >= i.all_ladder.top:
                stay_ladder = True
                return stay_ladder
        return stay_ladder
        
    def draw_ladders(self):
        for i in self.ladders:
            i.draw(self.screen)
        