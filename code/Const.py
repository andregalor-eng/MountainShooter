# C
import pygame

COLOR_ORANGE = (255, 128 ,0)
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)

# E
EVENT_ENEMY = pygame.USEREVENT +1
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Level1Bg5': 5,
    'Level1Bg6': 6,
    'PLayer1': 3,
    'PLayer2': 3,
    'Enemy1': 2,
    'Enemy2': 1,
}

# P
PLAYER_KEY_UP = {'PLayer1': pygame.K_UP,
                 'PLayer2': pygame.K_w}
PLAYER_KEY_DOWN = {'PLayer1': pygame.K_DOWN,
                 'PLayer2': pygame.K_s}
PLAYER_KEY_LEFT = {'PLayer1': pygame.K_LEFT,
                 'PLayer2': pygame.K_a}
PLAYER_KEY_RIGHT = {'PLayer1': pygame.K_RIGHT,
                 'PLayer2': pygame.K_d}
PLAYER_KEY_SHOOT = {'PLayer1': pygame.K_RCTRL,
                 'PLayer2': pygame.K_LCTRL}


# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT')

# S
SPAWN_TIME = 4000

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324