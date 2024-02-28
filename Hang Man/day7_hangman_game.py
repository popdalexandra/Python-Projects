#Here is the flowchart: https://drive.google.com/file/d/134gBSn2lonyUi0JtRUANsTwld2XO6LVm/view?usp=sharing

import random
from day7_hangman_game_art import stages, logo
from day7_hangman_game_words import word_list

print(logo)

chosen_word = random.choice(word_list)
len_chosen_word = len(chosen_word)
lives = 6 # keeps track of the number of lives.

# Create blanks - For each letter in the chosen_word, add a "_" to 'display'.
display = []
for _ in range(len_chosen_word):
  display += "_"
print(display)

# Let the user guess again. The loop stops once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_").
end_of_game = False

while not end_of_game :
    guess = input("Choose a letter: ").lower()

    if guess in display:
        print(f"The letter \"{guess}\" has already been used! Try another letter")

    # Check guessed letter - If the letter at that position matches 'guess' then reveal that letter in the display at that position.
    for pos in range(len_chosen_word):
        letter = chosen_word[pos]
        if letter == guess:
            display[pos] = letter
    # Check if user is wrong - If guess is not a letter in the chosen_word, Then reduce 'lives' by 1.
    if guess not in chosen_word:
        print(f"Sorry, the letter \"{guess}\" is not in this word! You have {lives - 1} lives!")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("you lose! :(")
            print(f"The word is: {chosen_word}")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win!")

    # print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])