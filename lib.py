import pygame
import random

SCREEN_SIZE = pygame.math.Vector2(1200, 900)

class Color():
    def __init__(self) -> object:
        self.BLACK = pygame.Color(0, 0, 0, 255)
        self.WHITE = pygame.Color(255, 255, 255, 255)
        self.RED = pygame.Color(255, 0, 0, 255)
        self.GREEN = pygame.Color(0, 255, 0, 255)
        self.BLUE = pygame.Color(0, 0, 255, 255)
        self.YELLOW = pygame.Color(255, 255, 0, 255)
        self.MAGENTA = pygame.Color(255, 0, 255, 255)
        self.CYAN = pygame.Color(0, 255, 255, 255)
        self.LIGHT_GRAY = pygame.Color(200, 200, 200, 255)
        self.MEDIUM_GRAY = pygame.Color(120, 120, 120, 255)
        self.DARK_GRAY = pygame.Color(50, 50, 50, 255)

    def get_random(self) -> pygame.Color:
        c = pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        return c
    
color = Color()

events = None

delta_time = 0
fps_limit = 120