import pyautogui, time
loop = int(input("how many times should you print the bee movie?"))
time.sleep(5)
for i in range(loop):
    f = open("test.txt", "r")
    output = ("looping the bee movie script:", loop, " times, currently on loop",i)
    print(output)
    for word in f:
        print(word)
        time.sleep(1)
        if word == " ":
            break
        pyautogui.typewrite(word)
        pyautogui.press("enter")
    f.close()