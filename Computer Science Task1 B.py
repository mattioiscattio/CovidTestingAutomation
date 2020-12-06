import random2
import sys

def game():
    lives = int(input("enter the number of lives that you want for the game"))
    highest_num = int(input("enter the highest value that the random number can take"))
    random_num = random2.randint(0, highest_num)

    for x in range(lives):
        lives -= 1
        print("enter your guess between 0 and ", highest_num)
        guess = int(input(""))

        if guess == random_num:
            print("you won the game with " , (lives) , "left")
            again = input("do you want to play again? y/n")

            if again == "y":
                game()

            else:
                print("closing the game")
                sys.exit()

        elif guess > random_num and guess <= highest_num:
            print("your guess was too high")
            print("your have " , (lives) , "lives left")

        elif guess < random_num and guess >= 0:
            print("your guess was too low")
            print("your have " , (lives) , "lives left")
        else:
            print("your awnser was out of the stated range, no help for you")
            print("your have " , (lives) , "lives left")

    print("your have run out of lives! the random number was" + (random_num))
    again = input("do you want to play again? y/n")

    if again == y:
        print("restarting the game")
        game()

    else:
        print("closing the game")
        sys.exit()

game()
