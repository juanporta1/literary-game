import pygame
import src.const as const
import images
import src.functions as functions
from src.button import Button
class Menu:

    def __init__(self,screen, type):
        
        self.play_button = Button(const.SCREEN_WIDTH / 2 - 150,const.SCREEN_HEIGHT / 2 - 50, 300, 100,"JUGAR","../assets/fonts/Crang16px.ttf",(255,255,255), (255,255,0),(0,0,0),0,screen)
        self.exit_button = Button(const.SCREEN_WIDTH / 2 - 150,const.SCREEN_HEIGHT / 2 + 50, 300, 100,"SALIR","../assets/fonts/Crang16px.ttf",(255,255,255), (255,255,0),(0,0,0),0,screen)
        
        self.screen = screen
        self.selected = 0
        self.menu_type = type
        self.run = True
    def call_inital_menu(self):
        
        self.run = True
        
        while self.run:
            self.screen.fill((0,0,0))
            pressed_key = pygame.key.get_pressed()
            mx, my = pygame.mouse.get_pos()
            
            if pressed_key[pygame.K_e]:
                self.run = False
               
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run =  False
                    
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.play_button.collidepoint(mx, my) or self.exit_button.collidepoint(mx, my):
                        self.run = False
                    
            
            pygame.display.update()