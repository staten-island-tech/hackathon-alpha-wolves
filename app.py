import pygame
import random
import time

# Initialize Pygame and the mixer
pygame.init()
pygame.mixer.init()

# Set up the game window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rhythm Game")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Game parameters
FPS = 60
obstacle_speed = 5
obstacle_frequency = 30  # The frequency at which obstacles spawn

# Score variables
score = 0
missed = 0

# List to store obstacles (notes)
obstacles = []

# Define the notes (obstacles)
class Note:
    def __init__(self, x, y, key):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.key = key  # Key that corresponds to this note (e.g., 'space', 'left', etc.)
        self.indicator_text = key.capitalize()  # Text to display beneath the note (e.g., 'Left', 'Right', etc.)

    def move(self):
        self.y += obstacle_speed

    def draw(self):
        pygame.draw.rect(screen, RED, (self.x, self.y, self.width, self.height))
        # Draw the key indicator text beneath the note
        font = pygame.font.Font(None, 36)
        indicator_text = font.render(self.indicator_text, True, WHITE)
        screen.blit(indicator_text, (self.x + self.width // 4, self.y + self.height + 5))  # Position the text below the note

# Function to handle score updates
def update_score(hit=True):
    global score, missed
    if hit:
        score += 10
    else:
        missed += 1
        score -= 5

# Load and play music
pygame.mixer.music.load("Thick_Of_It__feat__Trippie_Redd__[_YouConvert.net_].mp3")  # Replace with your audio file path
pygame.mixer.music.play(-1)  # Play music in a loop

# Timing variables
last_spawn_time = time.time()
beat_interval = 1  # This will define how often a new note will appear in seconds (simulating beat)

# Set up the clock for frame rate control
clock = pygame.time.Clock()

# Game States
countdown = 3  # Starting the countdown from 3
game_started = False

# Countdown Function
def show_countdown():
    global countdown
    font = pygame.font.Font(None, 100)
    countdown_text = font.render(str(countdown), True, WHITE)
    screen.blit(countdown_text, (WIDTH // 2 - 50, HEIGHT // 2 - 50))
    pygame.display.update()

    time.sleep(1)  # Wait 1 second for each countdown number
    countdown -= 1

# Main game loop
running = True
while running:
    screen.fill(BLACK)

    # Handle events (e.g., keypresses)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # Check for key presses matching the notes
            for note in obstacles:
                if note.key == pygame.key.name(event.key) and note.y >= HEIGHT - 100 and note.y <= HEIGHT - 50:
                    update_score(hit=True)  # Correct hit
                    obstacles.remove(note)  # Remove the note if hit

    # Countdown before the game starts
    if not game_started:
        if countdown > 0:
            show_countdown()  # Show countdown
        else:
            # Display "GO!" when countdown reaches 0
            font = pygame.font.Font(None, 100)
            go_text = font.render("GO!", True, WHITE)
            screen.blit(go_text, (WIDTH // 2 - 100, HEIGHT // 2 - 50))
            pygame.display.update()
            time.sleep(1)  # Wait 1 second for "GO!" to show up
            game_started = True  # Start the game

    # If the game has started, begin spawning and moving notes
    if game_started:
        # Spawn obstacles (notes) based on the beat (simulated)
        current_time = time.time()
        if current_time - last_spawn_time > beat_interval:
            # Randomly choose which key the player has to press
            key = random.choice(['left', 'right', 'up', 'down'])
            
            # Set note positions based on the key
            if key == 'left':
                note_x = 200
            elif key == 'right':
                note_x = 400
            elif key == 'up':
                note_x = 600
            elif key == 'down':
                note_x = 800  # Off the screen on the right, adjust if needed

            note_y = -50  # Start just above the screen
            obstacles.append(Note(note_x, note_y, key))
            last_spawn_time = current_time

        # Move and draw obstacles
        for note in obstacles:
            note.move()
            note.draw()

        # Check for missed notes (i.e., notes that go off the screen without being hit)
        for note in obstacles:
            if note.y > HEIGHT:
                update_score(hit=False)
                obstacles.remove(note)

        # Draw score and missed count
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, WHITE)
        missed_text = font.render(f"Missed: {missed}", True, WHITE)
        screen.blit(score_text, (10, 10))
        screen.blit(missed_text, (WIDTH - 150, 10))

    # Update the display
    pygame.display.update()

    # Control the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
