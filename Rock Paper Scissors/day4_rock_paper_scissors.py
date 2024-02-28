rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

print("Wellcome to Rock, Paper, Scissors game!\n")

print("Here are some rules: \nRock wins against scissors;\nPaper wins against rock; \nScissors wins against paper\n")

player = int(input("Let's start the game! Type 0 for Rock, 1 for Paper or 2 for Scissors!\n"))

if player == 0:
  print(f"Your Choice: {rock}")
elif player == 1:
  print(f"Your Choice: {paper} ")
elif player == 2:
  print(f"Your Choice: {scissors} ")
else:
  print("You should type 0, 1 or 2. Try again!\n")
  exit(0)

computer = random.randint(0, 2)

if computer == 0:
  print(f"Computer  Choice: {rock}")
elif computer == 1:
  print(f"Computer  Choice: {paper} ")
elif computer == 2:
  print(f"Computer  Choice: {scissors} ")

if  computer == player:
  print("Draw!")
elif (player == 0 and computer == 1) or (player == 1 and computer == 2) or (player == 2 and computer == 0):
  print("You lost! :(")
else: 
  print("You are the winner! :)")