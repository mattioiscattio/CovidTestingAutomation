import pygame
import sys
import random2
fullscreen = 0#0 for windowed, "pygame.FULLSCREEN" for fullscreen.
pygame.init()
character_posx = 500
character_posy = 290
screen = (1920, 1080)
clock = pygame.time.Clock()#defines clock to be used to manage time with clock.tick in the main game loop.
game = pygame.display.set_mode((screen), fullscreen, 32)#creates a display surface
game.fill((255, 255, 255))
full_screen_list = pygame.display.list_modes()#prints list of available fullscreen modes
while True:
    clock.tick(30)#runs game @30fps
    game.blit(pygame.transform.scale(pygame.image.load('mapsnip.png'), (1920, 1080)), (0,0))
    game.blit(pygame.image.load('Character_shadow.png'), (character_posx+6, (character_posy+18)))
    game.blit(pygame.image.load('Character.png'),(character_posx, character_posy))
    for event in pygame.event.get():#checks for events
        #print(event)
        if event.type == pygame.QUIT:#if the cross is clicked, closes program.
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                character_posy = character_posy - 5
            elif event.key == pygame.K_a:
                character_posx = character_posx - 5
            elif event.key == pygame.K_s:
                character_posy = character_posy + 5
            elif event.key == pygame.K_d:
                character_posx = character_posx + 5
    pygame.display.update()














































