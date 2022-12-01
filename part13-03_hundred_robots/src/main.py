# WRITE YOUR SOLUTION HERE:
import pygame

def print_line(x_otstup, y_otstup, width):
    i = 0
    while (i < 10):
        x = i * width + x_otstup
        window.blit(robot, (x, y_otstup))
        i+=1
    pygame.display.flip()

pygame.init()
window = pygame.display.set_mode((640, 480))
robot = pygame.image.load("robot.png")
window.fill((0, 0, 0))
width = robot.get_width()
x_otstup = 10
i = 0
y_otstup = 50
while (i < 10):
    print_line(x_otstup, y_otstup, width)
    x_otstup += 10
    y_otstup += 20
    i += 1
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()