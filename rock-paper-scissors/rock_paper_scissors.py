import random
import sys

player_score = 0
computer_score = 0

def game(player_score, computer_score):
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)

    player = None

    while player not in choices:
        player = input("Enter your choice (rock, paper, scissors): ").lower()
        if player not in choices:
            print("Choose from the bracket only...")

    print(f"You choose: {player.upper()}")
    print(f"Computer choose: {computer.upper()}")

    if player == computer:
        print("It's a Tie!")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("You Won!")
        player_score += 1
    else:
        print("You Lose!")
        computer_score += 1
    
    return player_score, computer_score
            

while True:
    player_score, computer_score = game(player_score, computer_score)

    print(f"--- SCORE: PLAYER {player_score} | COMPUTER {computer_score} ---")
    while True:
        choice = input("Do you want to continue playing (YES/NO): ").lower()
        if choice == "yes":
            break
        elif choice == "no":
            print("Thank You!")
            sys.exit()
        else:
            print("Please enter 'YES' or 'NO'.")