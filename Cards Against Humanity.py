import random2
import time

def play_again():
    game_loop()
    read_cards()
    point(test)

score = []
test = 1
black_cards = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
white_cards = [1, 2, 3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
player_list = []
cards_list = []
player_num = int(input("enter the number of people playing!"))

for x in range(player_num):#takes players names and adds them to player_list
    if player_list == []:#checks to see if the names list is empty, if so uses text "fist players name" instead of "next players name"
        player_name = input("enter the first players name!")
        player_list.append([player_name.title()])
        print(player_list)

    elif len(player_list) == player_num -1:#checks to see if the names list has 1 less than the total number of players and if so uses text "last players name" instead of "next players name"
        player_name = input("enter the last players name!")
        player_list.append([player_name.title()])
        print(player_list)

    else:
        player_name = input("enter the next players name!")
        player_list.append([player_name.title()])
        print(player_list)

def game_loop():
    #select random player for black card and give random black card, give other players random set of white cards(3?)
    white_cards2 = white_cards
    counter = 0
    bc_player = player_list[random2.randint(0, player_num-1)]
    bc_card = black_cards[random2.randint(0, len(black_cards)-1)]
    print(bc_player, "your get a black card which is", bc_card)
    #loop player amount of times, counter = 1, give player (counter) 3 cards, counter + 1

    #add random cards to cards_list
    for x in range(len(player_list)):
        counter2 = 0
        cards_list.append([])
        for x in range(3):
            list_remove_var = (random2.randint(0, len(white_cards2)-1))
            cards_list[counter].insert(counter2, [white_cards2[list_remove_var]])
            print(cards_list)
            print(white_cards2)
            print(counter)
            white_cards2.pop(list_remove_var)
            time.sleep(0.1)
            counter2+=1
        counter+=1
    print(player_list)

    #tell players their cards
def read_cards():
    counter = 1
    for x in range(len(player_list)):
        print(player_list[counter-1], "ready to read your cards?")
        read = input("press y to read cards!")
        if read == "y":
                print(cards_list[counter-1])
                counter +=1
        else:
                read_cards()

def point(test):
        #take winner of round
    round_winner = input("enter then name of the player that won")
    print(player_list)
    round_winner_temp = []

    """if round_winner not in score:
        round_winner_temp.append(round_winner)
        round_winner_temp.append(1)
        score.append(round_winner_temp)
        print(score)
    elif round_winner in score:
        x = score.index(round_winner)
        score[x] = score[x] + 1
        print(score)"""

    counter3 = 0
    if score:
        for x in range(len(player_list)):
            if round_winner in score[counter3]:
                score[counter3] += 1
                test = 0
                print(score)
            else:
                counter3 +=1
    elif test == 1:
        score.append([round_winner, 1])
        print(score)

    print("do you want to play again?")
    again = input("y/n")
    if again == "y":
        play_again()
    else:
        print("clsoing game")
        sys.exit()

play_again()