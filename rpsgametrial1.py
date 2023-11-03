import random

#list of choice options
possible_actions = ["rock", "paper", "scissors"]

#random choice for computer
rival_computer = possible_actions[randint(0,2)]

opponent = 1
computer_win=0
player_win=0

while opponent == 1:
#player choses its option
    opponent =  input('Choose your hand form: ')
    rival_computer = possible_actions[randint(0,2)]
    if opponent == rival_computer:
        print("Tie!")
        print("Score")
        print("computer win:",computer_win)
        print("player win:",player_win)
    elif opponent == "rock":
        if opponent == "paper":
            print("You lose! computer chose", rival_computer, "player chose", opponent)
            computer_win+=1
            print("Score")
            print("computer win:",computer_win)
            print("player win:",player_win)
             
        else:
            print("You win! player chose", opponent, "computer chose", rival_computer)
            player_win+=1
            print("Score")
            print("computer win:",computer_win)
            print("player win:",player_win)
    elif opponent == "paper":
        if rival_computer== "scissors":
            print("You lose! computer chose", rival_computer, "player chose", opponent)
            computer_win+=1
            print("Score")
            print("computer win:",computer_win)
            print("player win:",player_win)
        else:
            print("You win! player chose", opponent, "computer chose", rival_computer)
            player_win+=1
            print("Score")
            print("computer win:",computer_win)
            print("player win:",player_win)
    elif opponent == "scissors":
        if rival_computer == "rock":
            print("You lose computer chose", rival_computer, "player chose", opponent)
            computer_win+=1
            print("Score")
            print("computer win:",computer_win)
            print("player win:",player_win)
        else:
            print("You win! player chose",opponent, "computer chose", rival_computer)
            player_win+=1
            print("Score")
            print("computer win:",computer_win)
            print("player win:",player_win)
    else:
        print("That's not a valid play. Check your spelling!")