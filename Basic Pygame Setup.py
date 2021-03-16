import pygame
x = 0
screen_colour = (0, 230, 255)
screen_colour2 = (255, 0, 0)
rect_one = (0, 0, 100, 200)#defines x, y, width and height of the rectangle
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
        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:#if the event type is a key press and that key press is the w key then....
            x = "if this text shows then the input was correctly registered!"
            #screen.fill(screen_colour)#fills the window in turquoise
            #pygame.draw.rect(pygame.Surface.fill(screen_colour2), rect=None, special_flags=0, pygame.Color(screen_colour), pygame.rect(100, 100, 100, 200))
            pygame.draw.rect(screen, screen_colour, rect_one)#draws the rectangle, with parameters, surface(the window), color and x/y, width/height.
            pygame.display.update()#updates changes to the display




















