import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Create a display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Vib-Ribbon-like Game')

# Clock to control frame rate
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 50)
        self.velocity = 0
        self.gravity = 1  # Gravity for the player

    def update(self):
        # Apply gravity
        self.velocity += self.gravity
        self.rect.y += self.velocity

        # Prevent the player from falling through the ground
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
            self.velocity = 0

    def jump(self):
        # Make the player jump
        self.velocity = -15
        