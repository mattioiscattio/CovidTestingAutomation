#packages

import os
import pygame
from PIL import Image

#variables/basics

rgb_level = 0
bit_level = 0
run = True
read_x = 0
read_y = 0
mode = input("enter the mode you want to use, encode or decode")
bits_num = int(input("enter the number of bits you need to encode/decode"))
pygame.init()
clock = pygame.time.Clock()
image = Image.open(os.path.join("D:/Coding/PyCharm_Projects/Text Hider In Image/", "Base_Image.JPG")).resize((1920,1080)).save("Base_Image.JPG")
screen = pygame.display.set_mode((1920,1080), pygame.RESIZABLE)
screen.blit(pygame.image.load(os.path.join("D:/Coding/PyCharm_Projects/Text Hider In Image/", "Base_Image.JPG")), (0, 0))
pygame.display.flip()
bits = []
#functions

def encode(bit_level, rgb_level, bits_num, read_x):
    for x in range(bits_num):
        bit = int(input("enter the first/next/last bit"))
        bits.append(bit)
        print(bits, "this is the bit list")

    for x in range(bits_num//3):
        pixel_colors = screen.get_at((read_x, read_y))
        pixel_colors_changeable = list(pixel_colors)
        for x in range(3):
            if bits[bit_level] == 0 and ((pixel_colors_changeable[rgb_level] % 2) == 1):
                pixel_colors_changeable[rgb_level] = pixel_colors_changeable[rgb_level] - 1
                print(pixel_colors_changeable, bits[bit_level],"this is the rgb values being updated and then the bit being changed")
            elif bits[bit_level] == 1 and (((pixel_colors_changeable[rgb_level]) % 2) == 0):
                pixel_colors_changeable[rgb_level] -= 1
                print(pixel_colors_changeable, bits[bit_level], "this is the rgb values being updated and then the bit being changed")
            bit_level += 1
            rgb_level += 1
        pygame.draw.rect(screen, (tuple(pixel_colors_changeable)), (read_x, read_y, 1, 1))
        pygame.display.flip()
        read_x += 1
        rgb_level = 0
    bit_level = 0
    if bits_num != 0:
        for x in range(bits_num%3):
            if bits[bit_level] == 0 and ((pixel_colors_changeable[rgb_level] % 2) == 1):
                pixel_colors_changeable[rgb_level] = pixel_colors_changeable[rgb_level] - 1
                print(pixel_colors_changeable, bits[bit_level],
                      "this is the rgb values being updated and then the bit being changed")
            elif bits[bit_level] == 1 and (((pixel_colors_changeable[rgb_level]) % 2) == 0):
                pixel_colors_changeable[rgb_level] -= 1
                print(pixel_colors_changeable, bits[bit_level],
                      "this is the rgb values being updated and then the bit being changed")
            bit_level += 1
            rgb_level += 1
        pygame.draw.rect(screen, (tuple(pixel_colors_changeable)), (read_x, read_y, 1, 1))
        pygame.display.flip()
def decode():
    print("filler")

#main code

while run == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if mode.upper() == "ENCODE":
        print("entering encoding mode")
        encode(bit_level, rgb_level, bits_num, read_x)
        pygame.image.save(screen, "Encoded_Image.JPG")
        run = False
    elif mode.upper() == "DECODE":
        print("entering decoding mode")
        decode()
        pygame.image.save(screen, "Encoded_Image.JPG")
        run = False
    clock.tick(30)













































