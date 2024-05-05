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
        self.question_words = question.split()
        self.questions = []
        
        self.total_height = 0
        self.new_question = ""
        for word in self.question_words:
            proof = self.new_question + word + " "
            render_proof = self.font_question.render(self.new_question,0,(255,255,255))
            
            if render_proof.get_width() < self.box_question.width - 200:
                self.new_question = proof
            if render_proof.get_width() > self.box_question.width - 200 or word == self.question_words[-1]:
                self.new_question = proof
                question = self.font_question.render(self.new_question,0,(255,255,255))
                self.total_height += question.get_height()
                self.questions.append(question)
                self.new_question = ""  
            
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
            cont = 1
            actual_height = 0
            for i in self.questions:
                self.screen.blit(i, ((self.box_question.width - i.get_width()) / 2 + self.box_question.left, (self.box_question.height - self.total_height) / 2 + self.box_question.top + actual_height))
                actual_height += i.get_height()
                cont += 1
            for button in self.responses:
                if button.shape.collidepoint(mx,my):
                    button.selected = True
                else:
                    button.selected = False
                button.draw()
            
            pygame.display.update()  
            