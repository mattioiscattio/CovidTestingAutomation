import sys
from cryptography.fernet import Fernet, MultiFernet
#variable
option = "blank"

#functions
def readFile():
    passGuesser = open("passList.txt", "r")
    contents = passGuesser.read()
    passGuesser.close()
    return contents
def fileWipe():
    open("passlist.txt", "w").close()
def addToFile():
    passGuesser = open("passList.txt", "a+")
    loopNum = int(input("enter the number of passwords you want to add to the list"))

    for loop in range(loopNum):
        password = input("enter the password you want to add")
        passGuesser.write(str(len(open("passList.txt").readlines( )) + loop+ 1)+ password + "\n")
    passGuesser.close()
def decryption():
    line = 1
    inputHash = input("enter the hashed password that you want to find.")
    passGuesser = open("passList.txt", "r")

    for passCheck in passGuesser.readlines():

        if str(line) + inputHash + "\n" == passCheck:
            break

        elif str(line) + inputHash + "\n" != passCheck:
            print("tested", str(line) + inputHash, "as", passCheck, "returned false")
            line +=1

    print("the password is", passCheck[len(str(line)):-1], "found on line", passCheck[0:len(str(line))] )
    repeat = input("repeat for a different password? y/n")
    if repeat.upper() == "Y":
        decryption()


#main code
readFile()

while option.upper() != "WIPE" or "ADD" or "DECRYPT" "CLOSE":
    option = input("do you want to add to the password list or wipe it? type 'add' to add or 'wipe' to wipe it.\n You can also try to decrypt a hash using the password list by typing 'decrypt' \n you can also type close to exit the program.")
    if option.upper() == "WIPE":
        fileWipe()

    elif option.upper() == "ADD":
        addToFile()

    elif option.upper() == "DECRYPT":
        decryption()

    elif option.upper() == "CLOSE":

        sys.exit()