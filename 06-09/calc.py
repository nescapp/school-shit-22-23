# make snake with pygame
# 2019-04-08    PV

import pygame
import sys
import math
import random

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)

# Screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Snake size
SNAKE_WIDTH = 10
SNAKE_HEIGHT = 10

# Snake speed
SNAKE_SPEED = 10

# Snake direction
SNAKE_DIRECTION = 0

# Snake position
SNAKE_X = 0
SNAKE_Y = 0

# Snake body
SNAKE_BODY = []

# Snake food
SNAKE_FOOD = []

# Snake score
SNAKE_SCORE = 0

# Snake level
SNAKE_LEVEL = 1

# Snake level up
SNAKE_LEVEL_UP = 10

# Snake level up
SNAKE_LEVEL_UP_SPEED = 1

# Snake level up
SNAKE_LEVEL_UP_FOOD = 1

# Snake level up
SNAKE_LEVEL_UP_SCORE = 10

# Snake level up
SNAKE_LEVEL_UP_LEVEL = 1

