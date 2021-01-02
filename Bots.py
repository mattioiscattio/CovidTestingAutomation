import pyautogui, sys, os, time
from PIL import ImageGrab
import numpy as np
counter = 0
def chromeDinosaur():
    while True:
        capture = ImageGrab.grab()
        if capture.getpixel((780,330)) != (247,247,247):
            print("jumping")
            pyautogui.keyDown("up")
            pyautogui.keyUp("up")
        elif capture.getpixel((720,330)) != (247,247,247):
            print("jumping secondary")
            pyautogui.keyDown("up")
            pyautogui.keyUp("up")
        elif capture.getpixel((947,292)) != (247,247,247):
            pyautogui.keyDown("up")
            pyautogui.keyUp("up")
            print("restarting")

def mousePos():
    while True:
        print(pyautogui.position(), "this is the position")



def stormTheHouse():
    while True:
        game = ImageGrab.grab((40,599,1450,1079)).convert("L")
        #game.show()
        blackPixelProcessing(game)

def blackPixelProcessing(game):
    coordinates = np.column_stack(np.where(game < 1))
    print(coordinates)


def colourFinder(game):
    rgbgame = game.convert("RGB")
    for y in range(48):
        for x in range(140):
            pixel = rgbgame.getpixel((x*10, y*10))
            if pixel == ((0,0,0)):
                #print("black pixel found at: ",x*10+59, y*10+601)
                pyautogui.moveTo(x*10+70, y*10+601)
                pyautogui.click(x*10+70, y*10+601)
                #pyautogui.keyDown("space")





def iterationTest():#this loop test tests 1 in 10 pixels on the y and x axis, this is more efficeint but may be less accurate.
    while True:
        for y in range(48):
            for x in range(140):
                if y == 47:
                    print(x*5,y*5,"loop completed")




























def pixelFinder(width, hieght, colour, screen, left, top):
    for y in range(hieght):
        for x in range(width):
            if screen.getpixel((x+left,y+top)) == colour:
                print(x,y)
                time.sleep(3)
                return(x+left ,y+top)
    return ("pain")

decision = input("do you want to run the bot or get mousePos?\n enter mousePos or DINOSAUR or STH(storm the house)or IT(IterationTest) ")
if decision.upper() == "DINOSAUR":
    chromeDinosaur()
elif decision.upper() == "MOUSEPOS":
        mousePos()
elif decision.upper() == "STH":
    stormTheHouse()
elif decision.upper() == "IT":
    iterationTest()
