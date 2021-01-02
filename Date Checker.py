x = 0
def redo(x):
    again = input("do you want to play again? y/n")
    if again == "y":
        x = 0
        print("playing again!")
    elif again.lower == "n":
        x = 1
        print("Stopping Program")
    elif again != "y" or "n":
        print("incorrect input, stopping program")
        x = 1

while x == 0:
    day = int(input("enter the day of the month"))
    month = int(input("enter the month"))
    if day == 24 and month == 12:
        print("ITS CRHISTMAS EVE")
        redo(x)

    elif day >31 or month > 12:
        print("date incorrect")
        redo(x)
    else:
        print("its not christmas eve \n D:")
        redo(x)