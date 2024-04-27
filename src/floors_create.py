from src.floor import Floor
import pygame

class Floors_Create:
    
    def __init__(self, x, y, quantity, image, screen):
        self.floors = []
        self.initial_x = x
        self.initial_y = y
        self.actual_x = x
        self.quantity = quantity
        self.image = image
        self.screen = screen
        self.create_all_floors()
        
        
    def create_all_floors(self):
        for i in range(self.quantity):
            individual_floor = Floor(image=self.image, x=self.actual_x, y=self.initial_y)
            self.floors.append(individual_floor)
            self.actual_x += individual_floor.floor.width
            
        self.actual_x = self.initial_x
    
        print(self.floors)
    def draw_floors(self):
        
        for i in self.floors:
            i.draw(self.screen)
        
        
        
        