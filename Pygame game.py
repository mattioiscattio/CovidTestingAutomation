import time
import random2
import pygame

score = 0
mana = 0
#enemy_colour = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
rect_x_y = [400, 300]
rect_width_height = [20, 20]
width = 810
height = 610
running = False
background = (0,0,0)


def enemy1x_function():
    enemy1x_function = random2.randint(4, 78)
    return enemy1x_function

def enemy1y_function():
    enemy1y_function = random2.randint(4, 56)
    return enemy1y_function



def start(background, rect_x_y, rect_width_height, width, height, blue, red, mana,  score):
    running = True
    screen = pygame.display.set_mode((width, height))
    enemy1x = enemy1x_function()
    enemy1y = enemy1y_function()
    while running:
        print(rect_x_y, (enemy1x * 10), (enemy1y) * 10)
        time.sleep(0.0166)
        #time.sleep(0.1)
        mana = mana+1
        screen.fill((red))
        pygame.draw.rect(screen, background, (20, 20, width-40, height-40))
        pygame.draw.rect(screen, blue, (rect_x_y[0], rect_x_y[1], rect_width_height[0], rect_width_height[1]))#drawing the player
        print(mana)
        if mana >= 100:
            pygame.draw.rect(screen, (255, 255, 255), (750, 570, 30, 10))
        pygame.draw.rect(screen, (random2.randint(0,255), random2.randint(0,255), random2.randint(0,255)), (enemy1x*10, enemy1y*10, 20, 20))#drawing the first enemy

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and rect_x_y[0] < width-40:
                    rect_x_y[0] += 10
                    print(rect_x_y)
                elif event.key == pygame.K_LEFT and rect_x_y[0] > 20:
                    rect_x_y[0] -= 10
                    print(rect_x_y)
                elif event.key == pygame.K_UP and rect_x_y[1] > 20:
                    rect_x_y[1] -= 10
                    print(rect_x_y)
                elif event.key == pygame.K_DOWN and rect_x_y[1] < height-40:
                    rect_x_y[1] += 10
                    print(rect_x_y)
                elif event.key == pygame.K_w and rect_x_y[1] > 60 and mana >= 100 :
                    mana = mana - 100
                    for x in range (10):
                        rect_x_y[1] -= 5
                        pygame.draw.rect(screen, blue, (rect_x_y[0], rect_x_y[1], rect_width_height[0], rect_width_height[1]))
                        time.sleep(0.2)
                        if rect_x_y[0] == enemy1x*10 and rect_x_y[1] == enemy1y*10:
                            score += 1
                            enemy1x = enemy1x_function()
                            enemy1y = enemy1y_function()
                        pygame.display.update()

                elif event.key == pygame.K_a and rect_x_y[0] > 60 and mana >= 100 :
                    mana = mana - 100
                    for x in range (10):
                        rect_x_y[0] -= 5
                        pygame.draw.rect(screen, blue, (rect_x_y[0], rect_x_y[1], rect_width_height[0], rect_width_height[1]))
                        time.sleep(0.2)
                        if rect_x_y[0] == enemy1x*10 and rect_x_y[1] == enemy1y*10:
                            score += 1
                            enemy1x = enemy1x_function()
                            enemy1y = enemy1y_function()
                        pygame.display.update()
                elif event.key == pygame.K_s and rect_x_y[1] < 530 and mana >= 100 :
                    mana = mana - 100
                    for x in range (10):
                        rect_x_y[1] += 5
                        pygame.draw.rect(screen, blue, (rect_x_y[0], rect_x_y[1], rect_width_height[0], rect_width_height[1]))
                        time.sleep(0.2)
                        if rect_x_y[0] == enemy1x*10 and rect_x_y[1] == enemy1y*10:
                            score += 1
                            enemy1x = enemy1x_function()
                            enemy1y = enemy1y_function()
                        pygame.display.update()
                elif event.key == pygame.K_d and rect_x_y[0] < 730 and mana >= 100 :
                    mana = mana - 100
                    for x in range (10):
                        rect_x_y[0] += 5
                        pygame.draw.rect(screen, blue, (rect_x_y[0], rect_x_y[1], rect_width_height[0], rect_width_height[1]))
                        time.sleep(0.2)
                        if rect_x_y[0] == enemy1x*10 and rect_x_y[1] == enemy1y*10:
                            score += 1
                            enemy1x = enemy1x_function()
                            enemy1y = enemy1y_function()
                        pygame.display.update()





            print(event)
    if not running:
        print("you score was", score,"!")




print("starting")
time.sleep(1)
start(background, rect_x_y, rect_width_height, width, height, blue, red, mana, score)















