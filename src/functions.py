import src.const as const
import pygame
import screeninfo


def scale_individual_image(image,scalex,scaley):
    newImage = pygame.transform.scale(image, (image.get_width() * scalex, image.get_height() * scaley))
    return newImage
def scale_images_screen(image): 
    width_multiplication = const.SCREEN_WIDTH / const.SCREEN_RIGHT_WIDTH
    height_multiplication = const.SCREEN_HEIGHT / const.SCREEN_RIGHT_HEIGHT
    
    newImage = pygame.transform.scale(image, (int(image.get_width() * width_multiplication), int(image.get_height() * height_multiplication)))
    return newImage

def scale_ubication_x(var):

    var = (var * const.SCREEN_WIDTH) / const.SCREEN_RIGHT_WIDTH
    return var
def scale_ubication_y(var):

    var = (var * const.SCREEN_HEIGHT) / const.SCREEN_RIGHT_HEIGHT
    return var




    