import pygame
import sys
import math
from Money_Count import MoneyCounter

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 520

# Load the background, player, and enemy images
background_image = pygame.image.load("Finance test grass.jpeg")
player_image = pygame.image.load("John Pork.jpg")
player_image = pygame.transform.scale(player_image, (50, 50))

enemy_image = pygame.image.load("African boy.jpg")
enemy_image = pygame.transform.scale(enemy_image, (50, 50))

# Set up the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dot Movement Game")

# Set up the font for displaying money
font = pygame.font.SysFont("Comic Sans MS", 30)

# Player dot initial position and speed
player_x, player_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
player_speed = 5

# Enemy dot initial position (top left corner)
enemy_x, enemy_y = 100, 100
enemy_speed = 2

# Create an instance of MoneyCounter
money_counter = MoneyCounter()

# Function to check for collision between player and enemy
def is_collision(x1, y1, x2, y2, size=50):
    """Check if two objects collide based on their coordinates and size."""
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance < size

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Handle player key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_image.get_width():
        player_x += player_speed
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < SCREEN_HEIGHT - player_image.get_height():
        player_y += player_speed

    # Move the enemy dot towards the player
    if enemy_x < player_x:
        enemy_x += enemy_speed
    if enemy_x > player_x:
        enemy_x -= enemy_speed
    if enemy_y < player_y:
        enemy_y += enemy_speed
    if enemy_y > player_y:
        enemy_y -= enemy_speed

    # Check for collision
    if is_collision(player_x, player_y, enemy_x, enemy_y):
        print("Game Over!")
        pygame.quit()
        sys.exit()

    # Update the money counter
    money_counter.update()

    # Draw everything
    screen.blit(background_image, (0, 0))
    screen.blit(player_image, (player_x, player_y))
    screen.blit(enemy_image, (enemy_x, enemy_y))

    # Draw the money counter
    money_counter.draw(screen, font)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)
