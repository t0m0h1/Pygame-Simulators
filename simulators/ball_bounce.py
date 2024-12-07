import pygame
import sys

pygame.init()

# Screen Dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Basic PyGame Tutorial")

# Colors (R, G, B)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Game Clock
clock = pygame.time.Clock()

# Rectangle Variables
rect_x, rect_y = 300, 300
rect_width, rect_height = 50, 50
rect_speed = 5

# Game Loop
while True:
    # Handle Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move Rectangle with Arrow Keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rect_x -= rect_speed
    if keys[pygame.K_RIGHT]:
        rect_x += rect_speed
    if keys[pygame.K_UP]:
        rect_y -= rect_speed
    if keys[pygame.K_DOWN]:
        rect_y += rect_speed

    # Fill Screen with White
    screen.fill(BLACK)

    # Draw Rectangle
    pygame.draw.rect(screen, BLUE, (rect_x, rect_y, rect_width, rect_height))

    # Update Display
    pygame.display.flip()

    # Limit Frame Rate
    clock.tick(30)
