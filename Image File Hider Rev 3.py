#packages

import os
import pygame
from PIL import Image

#variables/basics

rgb_location = 0
bit_level = 0
run = True
read_x = 0
read_y = 0
mode = input("enter the mode you want to use, encode or decode")
bits_num = int(input("enter the number of bits you need to encode/decode"))
pygame.init()
clock = pygame.time.Clock()
image = Image.open(os.path.join("D:/Coding/PyCharm_Projects/Text Hider In Image/", "Base_Image.jpg"))
screen = pygame.display.set_mode((1920,1080))
screen.blit(pygame.image.load(os.path.join("D:/Coding/PyCharm_Projects/Text Hider In Image/", "Base_Image.jpg")), (0, 0))
pygame.display.update()
bits = []
#functions
def encode(bits_num, bit_level, rgb_location, read_x, read_y):
    for x in range(bits_num):
        bit_input = int(input("enter the bit that you want to encode"))
        bits.append(bit_input)
        print(bits)

    for x in range(bits_num//3):
        pixel_colors = screen.get_at((read_x, read_y))
        pixel_colors = list(pixel_colors)
        print(bits_num//3, "this is the number of time that the main loop will run")
        print(pixel_colors,"this is the original rgb levels tuple")
        for x in range(3):
            if bits[bit_level] == (pixel_colors[rgb_location])%2:
                print("both are odd or both are even no action taken")
                print(pixel_colors)
                print(bit_level, "this is the bit level(what position is the encoding bit being read from)")

            elif (bits[bit_level] == 1 and (pixel_colors[rgb_location])%2 == 0) or (bits[bit_level] == 0 and (pixel_colors[rgb_location])%2 == 1):
                print(pixel_colors[rgb_location] )
                pixel_colors[rgb_location] += 1
                print("the program detected that the bits do not line up and has changed them")
                print(pixel_colors)
                print(bit_level, "this is the bit level(what position is the encoding bit being read from)")
            bit_level += 1
            rgb_location += 1
        rgb_location = 0
        print(tuple(pixel_colors), "this is the tuple that will be drawn")
        pygame.draw.rect(screen, pixel_colors, (read_x + 1, read_y + 1, 1, 1))
        pygame.display.update()
        read_x += 1
    for x in range(bits_num%3):
        print(bits_num%3, "this is the number of times that the secondary loop will run")

def decode():
    print("filler")




#Main Code
while run == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if mode.upper() == "ENCODE":
        print("entering encoding mode")
        encode(bits_num, bit_level, rgb_location, read_x, read_y)
        pygame.display.flip()
        pygame.image.save(screen, "Encoded_Image.jpg")
        run = False
    elif mode.upper() == "DECODE":
        print("entering decoding mode")
        decode()
        run = False
    clock.tick(30)











































