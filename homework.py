# Make the minigame three: Rock Paper Scissors

# The computer plays rock paper scissors with you. 
# The program simulates one turn of rock paper scissors, 
# and prints if the player wins or loses after the player makes their move.

import random

choices = ["rock", "paper", "scissors"]

computer = random.choice(choices)
player = input("Choose rock, paper, or scissors: ")

print("Computer chose:", computer)

if player == computer:
    print("It's a tie!")

elif player == "rock" and computer == "scissors":
    print("You win!")

elif player == "paper" and computer == "rock":
    print("You win!")

elif player == "scissors" and computer == "paper":
    print("You win!")

elif player in choices:
    print("You lose!")

else:
    print("You can't choose that awnser!")



