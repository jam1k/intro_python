# WRITE YOUR SOLUTION HERE:
import pygame
def move_righ(robot):
    x = 0
    y = 0
    while (x+robot.get_width()<640):
        x += 1
        window.fill((0, 0, 0))
        window.blit(robot, (x, y))
        pygame.display.flip()

def move_down(robot):
    x = 640 - robot.get_width()
    y = 0
    while (y + robot.get_height() < 480):
        y += 1
        window.fill((0, 0, 0))
        window.blit(robot, (x, y))
        pygame.display.flip()
    
def move_left(robot):
    x = 640 - robot.get_width()
    y = 480 - robot.get_height()

    while (x > 0):
        x -= 1
        window.fill((0, 0, 0))
        window.blit(robot, (x, y))
        pygame.display.flip()

def move_up(robot):
    x = 0
    y = 480 - robot.get_height()

    while (y > 0):
        y -= 1
        window.fill((0, 0, 0))
        window.blit(robot, (x, y))
        pygame.display.flip()

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

x = 0
y = 0
velocity = 1
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    move_righ(robot)
    move_down(robot)
    move_left(robot)
    move_up(robot)

    clock.tick(60)