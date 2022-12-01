# WRITE YOUR SOLUTION HERE:

import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

window.fill((0, 0, 0))

width = robot.get_width()
height = robot.get_height()
i = 0
x = i * width + 5
while (i < 10):
    x = i * width + 20
    window.blit(robot, (x, 200))
    pygame.display.flip()
    i+=1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()