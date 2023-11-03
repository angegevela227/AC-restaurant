import random
#choiceofpossibleaction
possible_actions = ("rock", "paper", "scissors")
rival_computer = random.choice(possible_actions)

#possiblescore
computer_win=0
player_win=0

#condition
while computer_win <=3 or player_win <=3:
    if computer_win == 3 or player_win == 3:
        break
#player choses its option
    opponent =  input('Choose your hand form: ')
    rival_computer = random.choice(possible_actions)

    if opponent == rival_computer:
         print('its tie')
         print('rival score:',computer_win)
         print('opponent score:',player_win)
    elif opponent == 'paper' and rival_computer == 'rock':
            print('you win!')
            player_win+=1
            print('rival score:',computer_win)
            print('opponent score:',player_win)
    elif opponent == 'scissors' and rival_computer == 'paper':
            print('you win!')
            player_win+=1
            print('rival score:',computer_win)
            print('opponent score:',player_win)
    elif opponent == 'rock' and rival_computer == 'scissors':
            print('you win!')
            player_win+=1
            print('rival score:',computer_win)
            print('opponent score:',player_win)
    elif opponent == 'scissors' and rival_computer == 'rock':
            print('you lose,try again')
            computer_win+=1
            print('rival score:',computer_win)
            print('opponent score:',player_win)
    elif opponent == 'rock' and rival_computer == 'paper':
            print('you lose,try again')
            computer_win+=1
            print('rival score:',computer_win)
            print('opponent score:',player_win)
    elif opponent == 'paper' and rival_computer == 'scissors':
            print('you lose,try again')
            computer_win+=1
            print('rival score:',computer_win)
            print('opponent score:',player_win)          
    else:
            print('invalid given,try again')