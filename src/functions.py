import src.const as const
import pygame
import screeninfo

def scale_images(image): 
    width_multiplication = const.SCREEN_WIDTH / const.SCREEN_RIGHT_WIDTH
    height_multiplication = const.SCREEN_HEIGHT / const.SCREEN_RIGHT_HEIGHT
    
    newImage = pygame.transform.scale(image, (int(image.get_width() * width_multiplication), int(image.get_height() * height_multiplication)))
    return newImage