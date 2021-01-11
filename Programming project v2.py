import random
import sys
import time

def task1():
    score = 0
    run = True
    songList = [["first song example", "artist1"], ["second song example", "artist 2"], ["third song example", "artist 3"]]
    while run == True:
        correct = False
        songChoice = random.randint(0,len(songList)-1)
        endTitle = "".join ([title[0:2] for title in ((songList[songChoice][0]).split())])#iterates through the song title after splitting it into seperate words and then taking the first two letters of each word
        for attempt in range(2):
            print(endTitle, songList[songChoice][1])
            guess = input("enter your guess for the title")
            if guess.upper() == songList[songChoice][0].upper():#tests if the guess is correct
                print("correct")
                correct = True
                score += 1
                break
            else:
                print("incorrect.")
        if correct == False:
            failureSave = input("you failed!\nyour score was:"+ str(score)+ "\n save score? y/n")#asks if the player wants to save thier score
            if failureSave.upper() == "Y":
                name = input("enter your name")
                scoreSave = open("ProgrammingPorjectv2Scores.txt", "w+")
                scoreSave.write(str(score)+ " this score was achieved by:  "+ name + "\n")#adds the score to the txt document and saves it. try to add sorting to this document in future.
                scoreSave.close()
            repeat = input("play again? y/n")
            if repeat.upper() == "Y":
                task1()
            else:
                start(choice)

def task2():
    playerList = []#creates a list and then adds all the player names to it
    playerNum = int(input("enter the number of players in the game"))
    roundNum = int(input("enter the number of rounds to play"))
    for x in range(playerNum):
        playerName = input("enter player "+ str(x)+ "'s name")
        playerList.append([playerName, 0])
        print(playerList)

    for x in range(roundNum):
        for i in range(playerNum):#iterates through the players once per round
            time.sleep(0)
            diceTemp = 0
            dice1 = random.randint(1,6)
            dice2 = random.randint(1,6)
            diceTotal = dice1 + dice2
          #  print(playerList[i][0] , "rolled a " , dice1 , "and a " , dice2 , "with a total of" , (diceTotal))
            if diceTotal % 2 == 0:#checks if the dies add up to an even number
                diceTemp += 10
            elif diceTotal %2 != 0:#checks if the dies add up to an odd number
                diceTemp -= 5
            if dice2 == dice1:#checks if the dies == eachother
                diceTemp += random.randint(1,6)
            if playerList[i][1] < 0:#makes sure that no player score goes below 0
                diceTotal = 0
                playerList[i][1] = 0
            else:#creates a final point count regarding if the dies where odd etc and adds it to the players score
                diceTotal += diceTemp
            playerList[i][1] = int(playerList[i][1]) + diceTotal
    regulation = False
    ordered = False
    while ordered == False:
        ordered = False
        for i in range(playerNum-1):
            if playerList[i][1] < playerList[i+1][1]:#swaps the value of i in the list with the next value on if the next one is larger. uses no extra variable
                playerList[i][1] = playerList[i][1] + playerList[i+1][1]
                print(playerList)
                playerList[i+1][1] = playerList[i][1] - playerList[i+1][1]
                print(playerList)
                playerList[i][1] = playerList[i][1] - playerList[i+1][1]
                print(playerList)
                ordered = False
                regulation = False
            else:
                if regulation == True:#need to fix this section as it is messy but it means that the loop will only stop after the algorithm has looped through the entire score list, not just part of it
                    ordered = True
                    break
                else:
                    regulation = True
    print(playerList)
    print("the winner is: ",playerList[0][0], "with a score of:", playerList[0][1])
    repeat = input("play again? y/n")
    if repeat.upper() == "Y":
        print("starting task 2")
        task2()
    else:
        print("returning to menu")
        start(choice)

def task3():
    #Had to change slightly to allow for more than two players, now red > blac > yellow.
    R = False
    B = False
    Y = False
    cardList = [[],[],[]]
    playerList = []
    randomCardList = []
    playerNum = int(input("how many players are playing?"))

    for i in range(playerNum):
        playerName = input("enter the players name")
        playerList.append([playerName,0])
        print(playerList)

    for i in range(3):
        if R == False:
            R = True
            for x in range(10):
                cardList[0].append(str(x+1)+"R")
        else:
            break
        if B == False:
            B = True
            for x in range(10):
                cardList[1].append(str(x+1)+"B")
        else:
            break
        if Y == False:
            Y = True
            for x in range(10):
                cardList[2].append(str(x+1)+"Y")
        else:
            break
    print(cardList)
    for i in range(30//playerNum):
        roundCards = []
        for x in range(playerNum):
            card = pickCard(cardList)
            roundCards.append(card)
            print(roundCards[x], "this is the card for round:", i+1, "for player", x+1, roundCards,"this is the full list for this round so far")
            print(playerList)
            #add player "attributes" to a list for each round, if the player has a losing card, remove that player etc.
        for x in range (len(playerList)):

            print(str(roundCards[x])[3:4])
            print(roundCards,"this is the original list this round")
            print(sorted(roundCards), "this is the sorted list for this round")




def pickCard(cardList):
    colourChoice = random.randint(1, 3)
    numberChoice = random.randint(1, len(cardList[colourChoice])-1)
    print(str(cardList[colourChoice][numberChoice]), "this is card")

    cardList[colourChoice].remove(cardList[colourChoice][numberChoice])
    return 4













choice = "0"
def start(choice):
    while choice != "1" and choice != "2" and choice != "3" and choice != "exit":
        choice = input("choose what task to do, 1/2/3 or exit")
    if choice == "1":
        print("task 1 chosen")
        task1()
    elif choice == "2":
        print("task 2 chosen")
        task2()
    elif choice == "3":
        print("task 3 chosen")
        task3()
    elif choice == "exit":
        sys.exit()
start(choice)




