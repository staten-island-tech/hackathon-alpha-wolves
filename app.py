import pygame
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Background Example")
background = pygame.image.load('Project Image.jpg')
running = True
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            screen.blit(background, (0, 0))
            pygame.display.flip()
pygame.quit()
import random
import time

# Initialize Pygame
pygame.init()

# Define Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
FPS = 60
ARROW_SPEED = 5  # Speed at which arrows fall
KEY_MAP = {
    pygame.K_UP: 'Up Arrow',
    pygame.K_DOWN: 'Down Arrow',
    pygame.K_LEFT: 'Left Arrow',
    pygame.K_RIGHT: 'Right Arrow'
}

# Setup screen and clock
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Rhythm Game")
clock = pygame.time.Clock()

# Define arrow class
class Arrow(pygame.sprite.Sprite):
    def __init__(self, direction):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(100, SCREEN_WIDTH - 100), 0)
        self.direction = direction
    
    def update(self):
        self.rect.y += ARROW_SPEED
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()  # Remove the arrow if it goes off-screen

# Main Game Function
def game_loop():
    running = True
    score = 0
    arrows_group = pygame.sprite.Group()
    all_sprites_group = pygame.sprite.Group()

    last_arrow_time = time.time()

    while running:
        screen.fill((0, 0, 0))  # Clear the screen with black

        # Create new arrows at random intervals
        if time.time() - last_arrow_time > 1:  # Change interval as needed
            last_arrow_time = time.time()
            arrow_direction = random.choice([pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT])
            new_arrow = Arrow(arrow_direction)
            arrows_group.add(new_arrow)
            all_sprites_group.add(new_arrow)
        
        # Update the arrows
        all_sprites_group.update()

        # Handle events (key press, quit)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key in KEY_MAP:
                    for arrow in arrows_group:
                        if arrow.direction == event.key and arrow.rect.colliderect(pygame.Rect(250, SCREEN_HEIGHT - 50, 100, 100)):
                            # If the arrow matches the key pressed and it reaches the "hit" area
                            score += 1
                            arrow.kill()  # Remove arrow from screen
                            break

        # Draw all sprites
        all_sprites_group.draw(screen)

        # Display score
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        pygame.display.flip()  # Update the display
        clock.tick(FPS)  # Maintain the FPS

    pygame.quit()

# Run the game loop
game_loop()
pygame.mixer.music.load('your_song.mp3')
pygame.mixer.music.play()

# In the game loop, check the current time in the song and spawn arrows accordingly
current_time = pygame.mixer.music.get_pos() / 1000  # Get time in seconds
if current_time % 2 == 0:  # Example: spawn an arrow every 2 seconds
    new_arrow = Arrow(random.choice([pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]))
    arrows_group.add(new_arrow)
    all_sprites_group.add(new_arrow)

