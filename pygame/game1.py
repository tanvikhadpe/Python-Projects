"""
Simple pygame program to draw a circle on the screen.

PROBLEMS:

Problem 1:

* Change the color of the ball to red, blue and gray
* Try changing the RGB

Problem 2: 

Move the ball to the top-right corner.

Will the ball stay in the top-right corner if the size is changed to something else?


Problem 3:

Draw balls in all the 4 the corners.

Problem 4:

Draw a row full of balls.

Problem 5:

Fill the screen with balls.

"""
import pygame
pygame.init()

# Set the window size
size = 400, 400
screen = pygame.display.set_mode(size)

color = 255, 255, 0 # R G B
center = (200, 200)
radius = 25

pygame.draw.circle(screen, color, center, radius)

# display whatever is drawn so far
pygame.display.flip()

# wait for 3 seconds so that we can see the window
pygame.time.wait(3000)
