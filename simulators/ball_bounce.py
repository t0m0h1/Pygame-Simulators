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

# Rectangle Variables
ball_radius = 20
ball_x = SCREEN_WIDTH // 2
ball_y = SCREEN_HEIGHT // 2
ball_speed_x = 4
ball_speed_y = 4


running = True
while running:

    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), ball_radius)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BLACK)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()

