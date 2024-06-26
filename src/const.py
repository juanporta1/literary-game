import screeninfo


PLAYER_VELOCITY = 5
FPS = 60
SCREEN_COLOR = ( 80, 95, 106)
SCREEN_RIGHT_WIDTH = 1980
SCREEN_RIGHT_HEIGHT = 1080

for m in screeninfo.get_monitors():
    SCREEN_WIDTH = m.width
    SCREEN_HEIGHT = m.height
    
PLAYER_WIDTH = (80 * SCREEN_WIDTH) / SCREEN_RIGHT_WIDTH
PLAYER_HEIGHT = (180 * SCREEN_HEIGHT) / SCREEN_RIGHT_HEIGHT