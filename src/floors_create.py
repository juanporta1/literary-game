from src.floor import Floor
import pygame
import random
from src.functions import scale_ubication_x,scale_ubication_y,scale_images_screen

class Floors_Create:
    
    def __init__(self, x, y, quantity, images, screen,is_first_floor = False):
        self.floors = []
        self.initial_x = x
        self.initial_y = y
        self.actual_x = x
        self.quantity = quantity
        self.images = images
        self.screen = screen
        self.is_first_floor = is_first_floor
        self.all_floor = pygame.Rect(x, y, images[0].get_width() * quantity, images[0].get_height())
        self.create_all_floors()
        
        
    def create_all_floors(self):
        for i in range(self.quantity):
            if i == 0:
                individual_floor = Floor(image=self.images[0], x=self.actual_x, y=self.initial_y)
                self.floors.append(individual_floor)
                self.actual_x += individual_floor.floor.width
            elif i == self.quantity - 1:
                individual_floor = Floor(image=self.images[len(self.images) - 1], x=self.actual_x, y=self.initial_y)
                self.floors.append(individual_floor)
                self.actual_x += individual_floor.floor.width
            
            else:
                individual_floor = Floor(image=self.images[random.randint(1, len(self.images) - 2)], x=self.actual_x, y=self.initial_y)
                self.floors.append(individual_floor)
                self.actual_x += individual_floor.floor.width
            
        self.actual_x = self.initial_x

    def detect_floor(floors, player):
        stay_floor = False
        
        if floors[0].all_floor.top == player.shape.bottom:
            stay_floor = True
            return (stay_floor, floors[0].is_first_floor)
        else:
            for i in range(1, len(floors)):
                if floors[i].all_floor.top == player.shape.bottom and player.shape.left < floors[i].all_floor.right - 20 and player.shape.right > floors[i].all_floor.left + 20: 
                    stay_floor = True    
                    return (stay_floor, floors[i].is_first_floor)
                    
        return (stay_floor, False)
        
    def draw_floors(self):
        
        for i in self.floors:
            i.draw(self.screen)
        
        
        
        