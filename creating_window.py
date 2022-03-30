import pygame
from sys import exit

# Best way to think of pygame.init() is starting the engine of a car
pygame.init()

# Creating the display surface
width = 800
height = 400
screen = pygame.display.set_mode((width,height))
# setting the name of display window
pygame.display.set_caption("Tutorial")
# Creating clock object to help with frame rate
Clock = pygame.time.Clock()

while True:
    # Checking for any player input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # draw all our elements and ...
    # Everything will updated in this while loop

    # This will update our display surface we created outside the loop
    pygame.display.update()
    # This sets our frame rate at 60 FPS
    Clock.tick(60)