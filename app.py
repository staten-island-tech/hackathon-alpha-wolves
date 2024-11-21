import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 600, 400
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Game settings
block_size = 20
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)

# Snake class
class Snake:
    def __init__(self):
        self.body = [(100, 50), (80, 50), (60, 50)]
        self.direction = "RIGHT"

    def move(self):
        head_x, head_y = self.body[0]
        if self.direction == "RIGHT":
            head_x += block_size
        elif self.direction == "LEFT":
            head_x -= block_size
        elif self.direction == "UP":
            head_y -= block_size
        elif self.direction == "DOWN":
            head_y += block_size
        
        new_head = (head_x, head_y)
        self.body = [new_head] + self.body[:-1]

    def grow(self):
        tail_x, tail_y = self.body[-1]
        if self.direction == "RIGHT":
            new_tail = (tail_x - block_size, tail_y)
        elif self.direction == "LEFT":
            new_tail = (tail_x + block_size, tail_y)
        elif self.direction == "UP":
            new_tail = (tail_x, tail_y + block_size)
        elif self.direction == "DOWN":
            new_tail = (tail_x, tail_y - block_size)
        self.body.append(new_tail)

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(win, GREEN, pygame.Rect(segment[0], segment[1], block_size, block_size))

# Function to display message
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    win.blit(mesg, [width / 6, height / 3])

def gameLoop():
    game_over = False
    clock = pygame.time.Clock()
    snake = Snake()
    food = (random.randrange(1, (width // block_size)) * block_size, random.randrange(1, (height // block_size)) * block_size)

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and snake.direction != "RIGHT":
                    snake.direction = "LEFT"
                elif event.key == pygame.K_RIGHT and snake.direction != "LEFT":
                    snake.direction = "RIGHT"
                elif event.key == pygame.K_UP and snake.direction != "DOWN":
                    snake.direction = "UP"
                elif event.key == pygame.K_DOWN and snake.direction != "UP":
                    snake.direction = "DOWN"

        snake.move()

        # Check if snake collides with the wall or itself
        head_x, head_y = snake.body[0]
        if head_x < 0 or head_x >= width or head_y < 0 or head_y >= height or (head_x, head_y) in snake.body[1:]:
            game_over = True
            message("You Lost! Press Q-Quit or C-Play Again", RED)
            pygame.display.update()

        # Check if snake eats the food
        if (head_x, head_y) == food:
            snake.grow()
            food = (random.randrange(1, (width // block_size)) * block_size, random.randrange(1, (height // block_size)) * block_size)

        # Fill screen with black color
        win.fill(BLACK)
        snake.draw()

        # Draw food
        pygame.draw.rect(win, RED, pygame.Rect(food[0], food[1], block_size, block_size))

        pygame.display.update()

        # Set game speed
        clock.tick(snake_speed)

    pygame.quit()

