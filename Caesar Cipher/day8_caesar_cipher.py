from day8_art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# I duplicated in order not to have errors in words that contain the last letters of the alphabet
number = ['1','2', '3', '4', '5', '6', '7', '8', '9', '0']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# if the user enters a shift that is greater than the number of letters in the alphabet
if shift > 26:
    shift = shift % 26

def caesar(plain_text, shift_amount, direction):
    cipher_text = ""
    if direction == "decode":
        shift_amount *= -1
    for letter in plain_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_pos = position + shift_amount                             
            cipher_text += alphabet[new_pos]
        else:
            cipher_text += letter
    print(f"The {direction} text is {cipher_text}")

caesar(text, shift, direction)

restart = False
while not restart:
    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26
    caesar(text, shift, direction)
    
    rst = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if rst == "no":
        restart = True
        print("Goodbye !")





# OR WITH 2 FUNCTIONS:
# def encrypt (plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)  # the position of the letter in plain_text 
#         # index() only shows the position the element finds the first time
#         new_pos = position + shift_amount                             
#         new_letter = alphabet[new_pos]
#         cipher_text += new_letter
#     print(f"The encoded text is {cipher_text}")

# def decrypt (cipher_text, shift_amount):
#     plain_text = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter) 
#         new_pos = position - shift_amount                             
#         new_letter = alphabet[new_pos]
#         plain_text += new_letter
#     print(f"The decoded text is {plain_text}")
    
# # check if the user wanted to encrypt or decypt the message
# if direction == "encode":
#     encrypt(text, shift)
# elif direction == "decode": 
#     decrypt(text, shift)




