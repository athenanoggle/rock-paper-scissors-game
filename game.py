import random 

print("Rock, Paper, Scissors, Shoot!") 

#Prompt user for input
user_choice = input ("Choose 'rock' or 'paper' or 'scissors.': ")
print(user_choice)

#Computer choice (at random)

options= ["rock", "paper", "scissors"]

computer_choice = random.choice(options)
print(computer_choice)