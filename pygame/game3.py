import sys
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

balls = [
    {"x": 0, "y": 100, "dx": 5, "dy": 5},
    {"x": 100, "y": 100, "dx": 10, "dy": 10}
]

def paint_ball(ball):
    draw_ball(ball['x'], ball['y'])
    ball['x'] = ball['x'] + ball['dx']
    ball['y'] = ball['y'] + ball['dy']

    if ball['x'] < 0 or ball['x'] > w:
        ball['dx'] = -ball['dx']

    if ball['y'] < 0 or ball['y'] > h:
        ball['dy'] = -ball['dy']

def paint():
    global x
    screen.fill(BLACK)
    for ball in balls:
        paint_ball(ball)

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        paint()
        pygame.display.flip()
        pygame.time.wait(50)

main()
