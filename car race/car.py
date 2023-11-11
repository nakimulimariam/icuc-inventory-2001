import pygame
import sys
import random
import os

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Racing Game")

# Load images
car_image = pygame.image.load("car.jpg")  


# Set the path to the image file
image_path = "car.jpg"

# Check if the file exists
if os.path.exists(image_path):
    # Load the image
    car_image = pygame.image.load(image_path)
else:
    # Print an error message if the file is not found
    print(f"Error: The file '{image_path}' does not exist.")


# Set up the car
car_width = 50
car_height = 100
car_x = WIDTH // 2 - car_width // 2
car_y = HEIGHT - car_height - 10
car_speed = 5

# Set up the obstacles
obstacle_width = 50
obstacle_height = 50
obstacle_speed = 5
obstacle_frequency = 25
obstacles = []

# Clock to control the frame rate
clock = pygame.time.Clock()

# Function to draw the car
def draw_car(x, y):
    screen.blit(car_image, (x, y))

# Function to draw obstacles
def draw_obstacles(obstacles):
    for obstacle in obstacles:
        pygame.draw.rect(screen, RED, obstacle)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the car
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 0:
        car_x -= car_speed
    if keys[pygame.K_RIGHT] and car_x < WIDTH - car_width:
        car_x += car_speed

    # Move and create obstacles
    for obstacle in obstacles:
        obstacle.move_ip(0, obstacle_speed)

    obstacles = [obs for obs in obstacles if obs.bottom > 0]

    if random.randint(1, obstacle_frequency) == 1:
        obstacle_x = random.randint(0, WIDTH - obstacle_width)
        obstacle_y = -obstacle_height
        obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height)
        obstacles.append(obstacle_rect)

    # Check for collisions
    for obstacle in obstacles:
        if obstacle.colliderect(pygame.Rect(car_x, car_y, car_width, car_height)):
            print("Game Over!")
            pygame.quit()
            sys.exit()

    # Draw everything
    screen.fill(WHITE)
    draw_car(car_x, car_y)
    draw_obstacles(obstacles)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
