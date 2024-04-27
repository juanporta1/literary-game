import pygame
import src.const as const
class Menu:

    def __init__(self,screen):
        
        self.play_button = pygame.Rect(0 , 0, 500,100)
        self.exit_button = pygame.Rect(0 , 0, 500,100)
        self.play_button.center = (const.SCREEN_WIDTH / 2, int(const.SCREEN_HEIGHT / 3))
        self.exit_button.center = (const.SCREEN_WIDTH / 2, int(const.SCREEN_HEIGHT / 2))
        self.selected = 0
        self.options = [self.play_button, self.exit_button]
        self.actual_option = self.options[self.selected]
        self.arrow = pygame.Rect(self.actual_option.x - 220, self.actual_option.y, 220, 200)
        
        self.screen = screen
        
    
    def call_inital_menu(self):
        
        clock = pygame.time.Clock()
        run = True
        
        while run:
            self.screen.fill((0,0,0))
            clock.tick(const.FPS)
            pressed_key = pygame.key.get_pressed()
            
            pygame.draw.rect(self.screen,(255,0,0),self.play_button)
            pygame.draw.rect(self.screen,(255,0,0),self.exit_button)
            pygame.draw.rect(self.screen,(0,255,0),self.arrow)        
            
            if pressed_key[pygame.K_UP] and self.selected != 0:
                self.selected -= 1
            else:
                self.selected = len(self.options) - 1
                
            if pressed_key[pygame.K_DOWN] and self.selected != 1:
                self.selected += 1
            else: 
                self.selected = 0
                
            if pressed_key[pygame.K_ESCAPE]:
                run = False
                    
            pygame.display.update()