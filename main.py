import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Load the background and dot images using pygame
background_image = pygame.image.load("Finance test grass.jpeg")
dot_image = pygame.image.load("John Pork.jpg")
dot_image = pygame.transform.scale(dot_image, (50, 50))  # Adjust size as needed

# Set up the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dot Movement Game")

# Dot initial position
dot_x, dot_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
dot_speed = 5

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Handle key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and dot_x > 0:
        dot_x -= dot_speed
    if keys[pygame.K_RIGHT] and dot_x < SCREEN_WIDTH - dot_image.get_width():
        dot_x += dot_speed
    if keys[pygame.K_UP] and dot_y > 0:
        dot_y -= dot_speed
    if keys[pygame.K_DOWN] and dot_y < SCREEN_HEIGHT - dot_image.get_height():
        dot_y += dot_speed

    # Draw everything
    screen.blit(background_image, (0, 0))
    screen.blit(dot_image, (dot_x, dot_y))
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)