import pygame

pygame.mixer.init()

# Load a sound file (e.g., WAV, MP3)
sound = pygame.mixer.Sound('your_sound_file.wav')

sound.play()

# Keep the program running to allow sound to play
pygame.time.wait(2000)  # Wait for 2 seconds to allow the sound to finish