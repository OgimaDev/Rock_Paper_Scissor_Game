import random

print("Lets play a game of rock paper scissors\nInput 'End' to end game and see scores \nStart....\n\n")

game_options = ["Rock", "Paper", "Scissors"]
computer_option = random.choice(game_options)


player_option = False

computer_score = 0
player_score = 0


while True:
    player_option = input("Rock, Paper or  Scissors?").capitalize()
    ## Conditions of Rock,Paper and Scissors

    if player_option == computer_option:
        print("You both picked the same for a TIE!!!")

    elif player_option == "Rock":
        if computer_option == "Paper":
            print("Loser Loser!", computer_option, "destroys", player_option)
            computer_score+=1
        else:
            print("Winner Winner!", player_option, "breaks", computer_option)
            player_score+=1

    elif player_option == "Paper":
        if computer_option == "Scissors":
            print("Loser Loser!", computer_option, "slices", player_option)
            computer_score+=1
        else:
            print("Winner Winner!", player_option, "destroys", computer_option)
            player_score+=1

    elif player_option == "Scissors":
        if computer_option == "Rock":
            print("Loser Loser!", computer_option, "breaks", player_option)
            computer_score+=1
        else:
            print("Winner Winner!", player_option, "slices", computer_option)
            player_score+=1

    elif player_option=='End':
        print("Final Game Scores:")
        print(f"Computer Score:{computer_score}")
        print(f"Player Score:{player_score}")
        break


