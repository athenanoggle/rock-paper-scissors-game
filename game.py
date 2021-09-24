import os 
from dotenv import load_dotenv

load_dotenv()
x=os.getenv("PLAYER_NAME")
print (x)

import random 

print("Welcome 'player one' to Rock-Paper-Scissors!")

#Prompt user for input
user_choice = input ("Choose 'rock,' 'paper,' or 'scissors': ")
print ("User Choice:")
print(user_choice)

options = ["rock", "paper", "scissors"]

#User choice validation
if user_choice not in options:
    print ("Invalid choice. I am sorry. The game will now exit.")
    exit()

#Computer choice (at random)
computer_choice = random.choice(options)
print ("Computer Choice:")
print(computer_choice)

#Display of winner
if user_choice == computer_choice:
    print ("Both players selected the same. It's a tie.")
elif user_choice == "rock":
    if computer_choice == "scissors":
        print ("Rock smashes scissors. You win.")
    else: 
        print("Paper covers rock. You lose.")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("Paper covers rock. You win.")
    else:
        print("Scissors cut paper. You lose.")
elif user_choice == "scissors":
    if computer_choice == "paper":
        print("Scissors cut paper. You win.")
    else:
        print("Rock smashes scissors. You lose.")

print ("Thanks for playing. Play again!")

