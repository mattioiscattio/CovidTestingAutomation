import pyautogui, time
loop = int(input("how many times should you print the bee movie?"))
time.sleep(5)
for i in range(loop):
    time.sleep(5)
    f = open("Bee.txt", "r")

    for word in f:
        time.sleep(0.3)
        pyautogui.typewrite(word)
        pyautogui.press("enter")
    f.close()