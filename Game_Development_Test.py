
import pygame
import random

Width = 360
Hieght = 480
Fps = 60

pygame.init() #'starts' Pygame
pygame.mixer.init()#'starts'Pygame sound mixer
screen = pygame.display.set_mode((Width, Hieght))
pygame.display.set_caption("testing for da game ting")#The Name Of The Window
clock = pygame.time.clock()#handles/keeps track of speed/fps

#game loop, includes processing input(events), update and draw/render.
running = True
while running:
#run game updater
    clock.tick(Fps)
#process inputs
    for event in pygame.event.get():
    #check for closing window.
        if event.type == pygame.QUIT:
            running = False


#draw
screen.fill(0, 0, 255)
pygame.display.flip()#using double buffer(draw, then render, eg flipping a white board, must be after draw)


