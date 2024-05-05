import pygame
import src.const as const
import images
import src.functions as functions
from src.button import Button
class Menu:

    def __init__(self,screen, type, text1, text2):
        
        self.font = pygame.font.Font("assets/fonts/Crang16px.ttf",30)
        self.play_button = Button(const.SCREEN_WIDTH / 2 - 150,const.SCREEN_HEIGHT / 2 - 100, 300, 100,text1,self.font,(255,255,255), (55,55,55),(0,0,0),0,screen)
        self.exit_button = Button(const.SCREEN_WIDTH / 2 - 150,const.SCREEN_HEIGHT / 2 + 100, 300, 100,text2,self.font,(255,255,255), (55,55,55),(0,0,0),0,screen)
        
        self.action = self.font.render("PRESIONE",0,(255,255,255))
    
        self.screen = screen
        self.tick = pygame.time.get_ticks()
        self.menu_type = type
        self.run = True
    def call_inital_menu(self):
        selected = 2
        
        self.run = True
        while self.run:
            self.screen.fill((0,0,0))
            pressed_key = pygame.key.get_pressed()
            mx, my = pygame.mouse.get_pos()
            
            self.play_button.draw()
            self.exit_button.draw()

            if self.play_button.shape.collidepoint(mx,my):
               self.play_button.selected = True
               self.exit_button.selected = False
            if self.exit_button.shape.collidepoint(mx,my):
               self.play_button.selected = False
               self.exit_button.selected = True
                
            if pygame.time.get_ticks() - self.tick > 100:
                   
                if pressed_key[pygame.K_w] or pressed_key[pygame.K_UP]:
                    if selected == 0:
                        selected = 1
                        self.exit_button.selected = True
                        self.play_button.selected = False
                    else:
                        selected = 0
                        self.play_button.selected = True     
                        self.exit_button.selected = False   
                if pressed_key[pygame.K_s] or pressed_key[pygame.K_DOWN]:
                    if selected == 0:
                        selected = 1
                        self.exit_button.selected = True
                        self.play_button.selected = False
                    else:
                        selected = 0
                        self.play_button.selected = True 
                        self.exit_button.selected = False           
                self.tick = pygame.time.get_ticks()
            if pressed_key[pygame.K_e]:
                if selected == 0:
                    return True
                elif selected == 1:
                    return False  
            
            self.screen.blit(self.action,(const.SCREEN_WIDTH / 2 - self.action.get_width(), const.SCREEN_HEIGHT * .8))
            self.screen.blit(images.key_e, (const.SCREEN_WIDTH / 2 + images.key_e.get_width() / 2, const.SCREEN_HEIGHT * .8 - images.key_e.get_height() / 3))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run =  False
                    
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.play_button.shape.collidepoint(mx, my):
                        return True
                    if self.exit_button.shape.collidepoint(mx, my):    
                        return False

            pygame.display.update()