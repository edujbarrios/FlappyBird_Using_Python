import pygame
import random

# Initialize Pygame
pygame.init()

# Set the window size
WIN_WIDTH = 400
WIN_HEIGHT = 708

# Create the window
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

# Load the images
#Take in count that png specifications should be taken as '../../image.png'
#In case that you want to use the predifined images, excecute this code as it is
background_image = pygame.image.load("background.png")
bird_image = pygame.image.load("bird.png") #Must be an empty background png, otherwise, a the image would be squared
pipe_image = pygame.image.load("pipe.png")

# Set the bird's starting position and movement speed
bird_x = 50
bird_y = 250
bird_movement = 0

# Set the pipe's starting position and movement speed
pipe_x = 300
pipe_y = random.randint(-200, 200)
pipe_movement = -2

# Set the gravity
gravity = 0.25

# Set the game over flag to False
game_over = False

# Main game loop
while not game_over:
    # Check for user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = -5

    # Apply gravity to the bird
    bird_movement += gravity

    # Move the bird
    bird_y += bird_movement

    # Check for collision with the ground
    if bird_y > WIN_HEIGHT - 60:
        game_over = True

    # Move the pipe
    pipe_x += pipe_movement

    # Check for collision with the pipe
    if pipe_x < -52:
        pipe_x = 300
        pipe_y = random.randint(-200, 200)
    if (bird_x + 34 > pipe_x) and (bird_x < pipe_x + 52) and (bird_y < pipe_y + 420) and (bird_y + 24 > pipe_y):
        game_over = True

    # Draw the background
    screen.blit(background_image, (0, 0))

    # Draw the bird
    screen.blit(bird_image, (bird_x, bird_y))

    # Draw the pipe
    screen.blit(pipe_image, (pipe_x, pipe_y))

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
