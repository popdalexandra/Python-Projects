import os
from day12_art import logo
from random import randint

EASY_DIFFICULTY = 10
HARD_DIFFICULTY = 5

#Function to check user's guess against actual answer
def check_answer(guess, answer, turns):
    if guess > answer:
        print("To hight!")
        return turns - 1
    elif guess < answer:
        print("To low!")
        return turns - 1
    else:
        print(f"You got it wright! The answer is {answer}.")

#Fuction to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy or 'hard': ")

    if level == "easy":
        return EASY_DIFFICULTY        
    else: 
        return HARD_DIFFICULTY
       
def game():
    print(logo)
    #Choosing a random number between 1 and 100
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100")
    answer = randint(11, 100)

    #Let the user guess the number and difficulty
    turns = set_difficulty()
    
    #Repeat the guessing functionality
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)

        if turns == 0:
            print("You've run out of guesses, you lose.")
            return  # exit and stops the function
        
os.system('cls')
game()



   


