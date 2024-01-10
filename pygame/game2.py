
import pygame
pygame.init()

# Set the window size
size = 600, 500
w, h = size

screen = pygame.display.set_mode(size)

BLACK = 0, 0, 0
YELLOW = 255, 255, 0
r = 25

def draw_ball(x, y):
    center = (x, y)
    pygame.draw.circle(screen, YELLOW, center, r)

y = r
for x in range(r, w):
    screen.fill(BLACK)
    draw_ball(x, y)
    pygame.display.flip()
    pygame.time.wait(1)

# wait for 3 seconds so that we can see the window
pygame.time.wait(10000)
