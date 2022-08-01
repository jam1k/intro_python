# WRITE YOUR SOLUTION HERE:
from random import randrange
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))
robot = pygame.image.load("robot.png")
window.fill((0, 0, 0))
width = robot.get_width()
height = robot.get_height()

for i in range(1000):
    window.blit(robot, (randrange(640 - width), randrange(480 - height)))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()