import pygame
from src.player import Player
import images
from src.ladder import Ladder
import src.const as const
from src.floors_create import Floors_Create


def create_level_floors(floor_list):
    draw_floors = []
    for i in floor_list:
        floor = Floors_Create(i[0], i[1], i[2], i[3], i[4])
        draw_floors.append(floor)
    return draw_floors
        
def draw_list_floors(list):
    for i in list:
        i.draw_floors()  
class Level_1:
    
    def __init__(self, screen):
        self.screen = screen
        self.player = Player(x = 10,
                        y = 1080-64-100)
    def call_level_1(self):
        

        clock = pygame.time.Clock()
        

        level1_floors = [[0, 1024, 31, images.proof_floor, self.screen],
                        [0, 824, 16, images.proof_floor,self.screen],
                        [1152, 824, 16, images.proof_floor,self.screen]]

        floors = create_level_floors(level1_floors)
        ladder = Ladder(1010, 625, images.proof_ladder)
        run = True

        while run:
            self.screen.fill(const.SCREEN_COLOR)
            clock.tick(const.FPS)
            pressed_keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if pressed_keys[pygame.K_ESCAPE]:
                    run = False
            self.player.draw(self.screen,(255,255,0))
            self.player.move()
            draw_list_floors(floors)
            ladder.draw(self.screen)

            pygame.display.update()