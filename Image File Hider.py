#Imports
import pygame
import os
from PIL import Image
import pygame
import time
from PIL import Image
#Basics
bits = int(input("enter the number of bits of data you need to encode/decode"))
close = False
pygame.init()
screen = pygame.display.set_mode((1920, 1080), pygame.RESIZABLE)#creates display and sets parameters, resizable allows it to be resized/maximised.
clock = pygame.time.Clock()

#functions
def encode():
    Image.open(os.path.join("D:/Coding/PyCharm_Projects/Text Hider In Image/", "Base_Image.JPG")).resize(
        (1920, 1080)).save("Base_Image.jpg")
    screen.blit(pygame.image.load(os.path.join("D:/Coding/PyCharm_Projects/Text Hider In Image/", "Base_Image.JPG")), (0, 0))
    pygame.display.update()
    rgb_level = 0
    bit_list = []
    bit_level = 0
    read_x = 0
    read_y = 0
    run = True
    if run == True:
        for x in range(bits):
            bit_list.append(int(input("enter the binary code, 1 digit at a time")))
        print(bit_list)
        for x in range(bits // 3):
            tuple_convert_temp = []
            pixel_colors = screen.get_at((read_x, read_y))

            for x in range(3):
                if bit_list[bit_level] == 0:
                    color_list = list(pixel_colors)
                    color_list[rgb_level] = (color_list[rgb_level] // 2)
                    color_list[rgb_level] = (color_list[rgb_level] * 2)
                    print(color_list, "this is the rgb values div 2 times 2")
                    tuple_convert_temp.append(color_list[rgb_level])
                    print(tuple_convert_temp, "this is the temp tuple conversion list")
                    print(bit_list[bit_level], "this is the bit used above")

                elif bit_list[bit_level] == 1:
                    if pixel_colors[rgb_level] % 2 == 1:
                        tuple_convert_temp.append(0)
                        tuple_convert_temp[rgb_level] = pixel_colors[rgb_level]
                        print(tuple_convert_temp, "this is the temp tuple conversion list")
                        print(bit_list[bit_level])

                    elif pixel_colors[rgb_level] % 2 == 0:
                        tuple_convert_temp.append(0)
                        pixel_colors[rgb_level] += 1
                        tuple_convert_temp[rgb_level] = pixel_colors[rgb_level]
                        print(tuple_convert_temp, "this is the temp tuple conversion list")
                        print(bit_list[bit_level])
                rgb_level += 1
                bit_level += 1
            pygame.draw.rect(screen, tuple(tuple_convert_temp), (read_x, read_y, 1, 1))
            print(tuple_convert_temp, "this is the final rgb levels")
            pygame.display.update()
            read_x += 1
            rgb_level = 0
        pixel_colors = screen.get_at((read_x, read_y))
        tuple_convert_temp = list(pixel_colors)
        tuple_convert_temp.pop(3)
        for x in range(bits % 3):
            if bit_list[bit_level] == 0:
                #color_list = list(pixel_colors)
                tuple_convert_temp[rgb_level] = (tuple_convert_temp[rgb_level] // 2)
                tuple_convert_temp[rgb_level] = (tuple_convert_temp[rgb_level] * 2)
                #print(tuple_convert_temp, "this is the rgb values div 2 times 2")
                #tuple_convert_temp[rgb_level] = color_list[rgb_level]
                print(tuple_convert_temp, "this is the temp tuple conversion list")
                print(bit_list[bit_level], "this is the bit used above")

            elif bit_list[bit_level] == 1:
                if pixel_colors[rgb_level] % 2 == 1:
                    tuple_convert_temp[rgb_level] = pixel_colors[rgb_level]
                    print(tuple_convert_temp, "this is the temp tuple conversion list")
                    print(bit_list[bit_level], "this is the bit used above")

                elif pixel_colors[rgb_level] % 2 == 0:
                    tuple_convert_temp[rgb_level] = (pixel_colors[rgb_level]) + 1
                    print(tuple_convert_temp, "this is the temp tuple conversion list")
                    print(bit_list[bit_level], "this is the bit used above")

            rgb_level += 1
            bit_level += 1

        pygame.draw.rect(screen, tuple(tuple_convert_temp), (read_x, read_y, 1, 1))
        pygame.display.update()
        run = False
        print("finished")
        pygame.display.update()
        pygame.image.save(screen, "encoded_img.jpg")
def decode():
    Image.open(os.path.join("D:/Coding/PyCharm_Projects/Text Hider In Image/", "encoded_img.jpg")).resize(
        (1920, 1080)).save("encoded_img.jpg")
    screen.blit(pygame.image.load(os.path.join("D:/Coding/PyCharm_Projects/Text Hider In Image/", "encoded_img.jpg")),
                (0, 0))
    pygame.display.update()
    read_x = 0
    read_y = 0
    rgb_level = 0
    bit_list = []
    for x in range(bits//3):
        pixel_colors = screen.get_at((read_x, read_y))
        print(pixel_colors, "this is the temp store for rgb values")
        for x in range(3):
            if (int(pixel_colors[rgb_level]) %2) == 0:
                bit_list.append(0)
            elif (pixel_colors[rgb_level]%2)==1:
                bit_list.append(1)
            rgb_level += 1
        read_x += 1
        rgb_level = 0
    rgb_level = 0
    pixel_colors = screen.get_at((read_x, read_y))
    pixel_colors = list(pixel_colors)
    pixel_colors.pop(3)
    print(pixel_colors, "this is the temp store for rgb values")
    for x in range(bits%3):
        print(bits%3, "this is the number of times the second loop will iterate")
        if (pixel_colors[rgb_level] % 2) == 0:
            bit_list.append(0)
        elif (pixel_colors[rgb_level] % 2) == 1:
            bit_list.append(1)
        rgb_level += 1
    return bit_list
#main Code
tuple_convert_temp = []
rgb_level = 0
Image.open(os.path.join("D:/Coding/PyCharm_Projects/Text Hider In Image/", "Base_Image.JPG")).resize((1920, 1080)).save("Base_Image.jpg")
screen.blit(pygame.image.load(os.path.join("D:/Coding/PyCharm_Projects/Text Hider In Image/", "Base_Image.JPG")), (0, 0))
pygame.display.update()

while close == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:#if cross clicked
            close = True
    mode = input("enter the mode you want to use, Encode or Decode.")
    if mode.upper() == "ENCODE":
        encode()
    elif mode.upper() == "DECODE":
        print(decode(), "this is the decoded data in binary")
    rerun = input("run again? y/n")
    if rerun.upper() == "Y":
        close = False
    elif rerun.upper() == "N":
        close = True
    clock.tick(30)#runs window @ 30fps
















