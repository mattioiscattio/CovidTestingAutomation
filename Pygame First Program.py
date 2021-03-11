import pygame
x = 0

game = input("do you want to start the game? y/n")
while game.upper() == "Y":
    pygame.init()  # starts pygame
    width = 800
    height = 600
    screen = pygame.display.set_mode((width, height))# defines what the screen is
    for event in pygame.event.get():#takes inputs
        print(event)
        if event.type == pygame.QUIT:#if the cross is clicked, closes the window.
            game = "n"#pauses the while loop.
            print(x)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            x = "if this text shows then the input was correctly registered!"
            pygame.draw.rect(pygame.Surface.fill((0, 230, 255), rect=None, special_flags=0), pygame.Color(0, 230, 255), pygame.rect(100, 100, 100, 200))





















