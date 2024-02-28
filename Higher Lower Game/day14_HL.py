from day14_art import logo, vs
from day14_game_data import data
import random
import os

print(logo)
score = 0
game_should_continue = True

# Format the account data into a printable format
def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

# Check if the user is correct
def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == 'a' # True if guess == 'a' else False if guess != 'a'
    else:
        return guess == 'b'

 # Making accounnt at position B become the next account at position A
account_b = random.choice(data)

# Make the game repetable
while game_should_continue:

    # Generate a random account from the game data
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    # Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check if the user is correct
    ## Get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    # Clear the screen
    os.system('cls')
    print(logo)

    # Give user feedback on their guess
    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    if is_correct:
        score +=1
        print(f"You're right! Currentt score: {score}")
        
    else: 
        game_should_continue = False
        print(f"Sorry, You're wrong! Final score {score}")




