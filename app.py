import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Define Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
FPS = 60
ARROW_SPEED = 5  # Initial speed at which arrows fall
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

# Load background image
background = pygame.image.load('photo.webp')  # Make sure to replace with your actual background file path
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))  # Scale it to fit the screen

# Define arrow class
class Arrow(pygame.sprite.Sprite):
    def __init__(self, direction):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 255, 0))  # Arrow color (green)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(100, SCREEN_WIDTH - 100), 0)
        self.direction = direction

    def update(self):
        global ARROW_SPEED  # Use the global variable for arrow speed
        self.rect.y += ARROW_SPEED
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()  # Remove the arrow if it goes off-screen

# Main Game Function
def game_loop():
    global ARROW_SPEED  # Access the global variable to modify the speed
    running = True
    score = 0
    arrows_group = pygame.sprite.Group()
    all_sprites_group = pygame.sprite.Group()

    # Load and play music
    pygame.mixer.music.load('baby-shark-dance-sing-and-dance-baby-shark-official-pinkfong-songs-for-children-XqZsoesa55w.mp3')  # Make sure your song path is correct
    pygame.mixer.music.play(-1, 0.0)  # Play the song indefinitely

    start_time = time.time()  # Record the start time of the game

    # Game loop
    while running:
        screen.fill((0, 0, 0))  # Clear the screen with black (though the background will cover this)
        
        # Display the background image
        screen.blit(background, (0, 0))  

        
        current_time = pygame.mixer.music.get_pos() / 1000  

        
        elapsed_time = time.time() - start_time  
        ARROW_SPEED = 5 + (elapsed_time // 10)  

        
        if int(current_time) % 2 == 0 and len(arrows_group) < 5:  
            arrow_direction = random.choice([pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT])
            new_arrow = Arrow(arrow_direction)
            arrows_group.add(new_arrow)
            all_sprites_group.add(new_arrow)

        
        all_sprites_group.update()

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key in KEY_MAP:
                    for arrow in arrows_group:
                        
                        if arrow.direction == event.key:
                            if arrow.rect.colliderect(pygame.Rect(250, SCREEN_HEIGHT - 50, 100, 100)):
                                score += 1
                                arrow.kill()  
                                break

        
        font = pygame.font.SysFont(None, 48)
        if arrows_group:  
            arrow_direction = arrows_group.sprites()[0].direction  
            instruction_text = "Press " + KEY_MAP[arrow_direction]
            instruction_surface = font.render(instruction_text, True, (255, 255, 255))
            screen.blit(instruction_surface, (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 4))

       
        all_sprites_group.draw(screen)

        
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(150, SCREEN_HEIGHT - 50, 100, 100))  
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(250, SCREEN_HEIGHT - 50, 100, 100))  
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(350, SCREEN_HEIGHT - 50, 100, 100))  
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(450, SCREEN_HEIGHT - 50, 100, 100))  

        
        pygame.draw.line(screen, (255, 255, 255), (250, SCREEN_HEIGHT), (250, 0), 3)

        pygame.display.flip() 
        clock.tick(FPS)  

    pygame.quit()


game_loop()
