import src.functions as functions
import pygame
import src.const as const
from src.button import Button


class Question:
    
    def __init__(self,question, texts_responses, true,screen):
        self.box_question = pygame.Rect(50,50,const.SCREEN_WIDTH - 100, const.SCREEN_HEIGHT / 2 - 50)
    
        self.font_response = pygame.font.Font("assets/fonts/Minecraftia-Regular.ttf", 16)
        self.font_question = pygame.font.Font("assets/fonts/Minecraftia-Regular.ttf", 25)
        self.screen = screen
        self.question = self.font_question.render(question,0,(255,255,255))
        self.response_one = Button(50, const.SCREEN_HEIGHT / 2 + 50, const.SCREEN_WIDTH / 2 - 100, const.SCREEN_HEIGHT / 4 - 100, texts_responses[0], self.font_response, (55,55,55), (25,25,25), (235,235,235), False,self.screen)
        
        self.response_two = Button(const.SCREEN_WIDTH / 2 + 50, const.SCREEN_HEIGHT / 2 + 50, const.SCREEN_WIDTH / 2 - 100, const.SCREEN_HEIGHT / 4 - 100, texts_responses[1], self.font_response, (55,55,55), (25,25,25), (235,235,235), False,self.screen)
        
        self.response_three = Button(50, (const.SCREEN_HEIGHT- (const.SCREEN_HEIGHT / 4)) + 50, const.SCREEN_WIDTH / 2 - 100, const.SCREEN_HEIGHT / 4 - 100, texts_responses[2], self.font_response, (55,55,55), (25,25,25), (235,235,235), False,self.screen)
        
        self.response_four = Button(const.SCREEN_WIDTH / 2 + 50, (const.SCREEN_HEIGHT- (const.SCREEN_HEIGHT / 4)) + 50, const.SCREEN_WIDTH / 2 - 100, const.SCREEN_HEIGHT / 4 - 100, texts_responses[3], self.font_response, (55,55,55), (25,25,25), (235,235,235), False,self.screen)
        self.responses = [self.response_one,self.response_two,self.response_three,self.response_four]
        
        self.responses[true].value = True
        
    def draw(self):
        
        run = True
        
        while run:
            self.screen.fill((0,0,0))
            
            mx,my = pygame.mouse.get_pos()
            
            
            
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for button in self.responses:
                        if button.shape.collidepoint(mx,my):
                            run = False
                            return button.value

            pygame.draw.rect(self.screen,(66,66,66),self.box_question)
            self.screen.blit(self.question, ((self.box_question.width - self.question.get_width()) / 2 + self.box_question.left, (self.box_question.height - self.question.get_height()) / 2 + self.box_question.top))
            for button in self.responses:
                if button.shape.collidepoint(mx,my):
                    button.selected = True
                else:
                    button.selected = False
                button.draw()
            
            pygame.display.update()
            
        
        
            
            
        
        
        
            
            