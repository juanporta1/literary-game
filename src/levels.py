import pygame
from src.player import Player
import images
from src.ladder import Ladder
import src.const as const
from src.floors_create import Floors_Create
from src.ladders_create import Ladders_Create
import src.functions as functions
from src.menu import Menu
from src.functions import scale_ubication_x,scale_ubication_y,scale_images_screen
from src.questions import Question

def create_level_floors(floor_list):
    draw_floors = []
    for i in floor_list:
        floor = Floors_Create(i[0], i[1], i[2], i[3], i[4], i[5])
        draw_floors.append(floor)
    return draw_floors

def create_level_ladders(ladder_list):
    draw_ladders = []
    for i in ladder_list:
        ladder = Ladders_Create(i[0], i[1], i[2], i[3], i[4])
        draw_ladders.append(ladder)
    return draw_ladders
        
def draw_list_floors(list):
    for i in list:
        i.draw_floors() 

def draw_list_ladders(list):
    for i in list:
        i.draw_ladders() 
        
class Door:
    
    def __init__(self,x,y,screen):   
        self.shape = pygame.Rect(scale_ubication_x(x),scale_ubication_y(y),100, 200)
        self.enabled = False
        self.screen = screen
        self.green_arrow = images.green_arrow
        self.red_arrow = images.red_arrow
        self.arrow_position = [self.shape.centerx - 100, self.shape.centery - self.red_arrow.get_height() / 2]
        self.clock = pygame.time.get_ticks()
        self.count = 0
    def draw(self):
        self.arrows_animations()
        if self.enabled:
            self.screen.blit(self.green_arrow, (self.arrow_position))
        else:
            self.screen.blit(self.red_arrow, (self.arrow_position))
            
    def arrows_animations(self):
        frame_time = 40
        if (pygame.time.get_ticks() - self.clock) > frame_time:
            if self.count <= 10:
                if self.count <= 5:
                    self.arrow_position[0] -= 5
                elif self.count <= 10:
                    self.arrow_position[0] += 5
                self.count += 1
            elif self.count <= 20:
                if self.count <= 15:
                    self.arrow_position[0] += 5
                elif self.count <= 20:
                    self.arrow_position[0] -= 5
                self.count += 1
            if self.count == 20:
                self.count = 0
            self.clock = pygame.time.get_ticks()

class Key:
    def __init__(self, x, y, screen, door,question): 
        self.shape = pygame.Rect(scale_ubication_x(x),scale_ubication_y(y),50,50)
        self.enabled = False
        self.screen = screen
        self.door = door
        self.question = question
        
    def catch(self,player):
        pressed_key = pygame.key.get_pressed()
        if self.shape.colliderect(player) and not self.enabled:
            self.screen.blit(functions.scale_images_screen(functions.scale_individual_image(images.key_e,2,2)), (const.SCREEN_WIDTH/2 - functions.scale_images_screen(images.key_e).get_width() / 2, 900 ))
            
        if self.shape.colliderect(player) and pressed_key[pygame.K_e]:
            selection = self.question.draw()
            if selection:
                self.enabled = True
                self.door.enabled = True
            
        if not self.enabled:
            pygame.draw.rect(self.screen,(0,255,255),self.shape)    
        
        self.door.draw()
        
class Level:
    def __init__(self,screen):
        self.screen = screen
        self.run = True 
        self.next_level = 1
        self.menu = Menu(self.screen, 2,"CONTINUAR", "SALIR") 
        

    
class Level_1(Level):
    
    def __init__(self, screen):
        super().__init__(screen)
        self.player = Player(x = 10, y = 835)
        self.main_door = Door(1820,815,self.screen)
        self.main_question = Question("¿Cuál es el impacto de la inteligencia artificial en la sociedad moderna y cómo puede influir e la economía global en las próximas décadas, considerando aspectos éticos, políticos y tecnológicos?",["uno", "dos", "verdadera","cuatro"],2,self.screen)
        self.main_door_key = Key(30,700,self.screen,self.main_door,self.main_question)
        
    
        
    def call_level_1(self):
     
        clock = pygame.time.Clock()
   
        level1_floors = [[0, 1015, 31, [images.mid_wood_floor,images.mid_wood_floor,images.mid_wood_floor], self.screen,True],
                        [0, 750, 16,[images.mid_wood_floor,images.mid_wood_floor,images.mid_wood_floor],self.screen,False],
                        [1155, 750, 15,[images.mid_wood_floor,images.mid_wood_floor,images.mid_wood_floor],self.screen,False]]
        
        level1_ladders = [[1040, 1015, 2, images.common_ladder,self.screen]]

        floors = create_level_floors(level1_floors)
        ladders = create_level_ladders(level1_ladders)
        
        
        self.run = True
        while self.run:
            
            self.screen.fill(const.SCREEN_COLOR)
            clock.tick(const.FPS)
            pressed_keys = pygame.key.get_pressed()
            
            if pressed_keys[pygame.K_ESCAPE]:
                    option = self.menu.call_inital_menu()
                    if not option:
                        self.run = option
                        continue
                    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

            draw_list_floors(floors)
            draw_list_ladders(ladders)
            self.main_door_key.catch(self.player.shape)
            
            stay_floor, is_first_floor = Floors_Create.detect_floor(floors, self.player)
            stay_ladder = Ladders_Create.detect_ladder(ladders, self.player)    
                
            self.player.draw(self.screen,(255,255,0))    
            self.player.move(stay_floor, is_first_floor, stay_ladder)    
            
            if self.main_door.shape.colliderect(self.player.shape) and self.main_door.enabled:
                self.run = False   
                self.next_level = 2
                return self.next_level
        
            
            pygame.display.update()

        
class Level_2(Level):
    
    def __init__(self, screen):
        super().__init__(screen)
        self.player = Player(x = 10, y = 1080 - 65 - 180)
        self.door1 = Door(1820,815,self.screen)
        self.main_question = Question("¿Holaa?",["falsa", "falsa", "verdadera","falsa"],2,self.screen)
        self.door1_key = Key(30,700,self.screen,self.door1,self.main_question)
        
        
    def call_level_2(self):
        clock = pygame.time.Clock()
        while self.run:
            self.screen.fill(const.SCREEN_COLOR)
            clock.tick(const.FPS)
            pressed_keys = pygame.key.get_pressed()
            
            if pressed_keys[pygame.K_ESCAPE]:
                    self.run = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
            self.verify_selection(self.run)
            pygame.display.update()