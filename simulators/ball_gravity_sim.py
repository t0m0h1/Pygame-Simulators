import pygame
import sys

pygame.init()

# Screen Dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ball Simulation")


# Colors (R, G, B)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Game Clock
clock = pygame.time.Clock()


# Ball properties
ball_radius = 20
ball_x = SCREEN_WIDTH // 2
ball_y = SCREEN_HEIGHT // 2


# Physics constants
gravity = 0.5  # Acceleration due to gravity
friction = 0.99  # Friction slows the ball
bounce_factor = -0.8  # Energy lost on bounce





running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(BLACK)
    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), ball_radius)  
    pygame.display.flip()  # Update the display
    clock.tick(60)  # Limit to 60 frames per second

pygame.quit()
sys.exit()
