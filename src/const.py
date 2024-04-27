import screeninfo

PLAYER_WIDTH = 50
PLAYER_HEIGHT = 100
PLAYER_VELOCITY = 5
FPS = 60
SCREEN_COLOR = ( 80, 95, 106)
SCREEN_RIGHT_WIDTH = 1980
SCREEN_RIGHT_HEIGHT = 1080

for m in screeninfo.get_monitors():
    SCREEN_WIDTH = m.width
    SCREEN_HEIGHT = m.height
    
print(SCREEN_HEIGHT)