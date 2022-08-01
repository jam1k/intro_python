# WRITE YOUR SOLUTION HERE:
import pygame
import time

class Robot():
    def __init__(self, window, myimage, x_coordinates, y_coordinates, velocity):
        self.window = window
        self.image = myimage
        self.x_coordinates = x_coordinates
        self.y_coordinates = y_coordinates
        self.velocity = velocity
    
    def display_robot(self):
        
        window.blit(self.image, (self.x_coordinates, self.y_coordinates))
        pygame.display.flip()
       
    
    def move(self):
        

        self.x_coordinates += self.velocity
        if self.velocity > 0 and self.x_coordinates + self.image.get_width() >= 640:
            self.velocity = -self.velocity
        if self.velocity < 0 and self.x_coordinates <= 0:
            self.velocity = -self.velocity
    


pygame.init()
window = pygame.display.set_mode((640, 480))
robot = pygame.image.load("/Users/jamilya/Library/Application Support/tmc/vscode/mooc-programming-22/part13-07_two_robots/src/robot.png")

robot1 = Robot(window, robot, 0, 15, 1)
robot2 = Robot(window, robot, 0, 150, 2)

clock = pygame.time.Clock()
       
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    
    window.fill((0, 0, 0))
    robot1.move()
    

    robot2.move()
    
    robot1.display_robot()
    robot2.display_robot()
    
    clock.tick(60)
    