#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")



direction = input("You are at a cross road. Where do you want to go? Type \"left\" or \"right\". ").lower()

if direction == "right":
    print("Fall into a hole. Game Over!")
elif direction == "left":
  print("You came to a lake. There is an island in the middle of the lake.")
  activity = input("Type \"wait\" to wait for the boat or type \"swim\" to swim across.").lower()
  
  if activity == "swim":
    print("Attacked by trout. Game Over!")
  elif activity == "wait":
    print("You arrive at the island unharmed. There is a house with 3 doors: red, yellow and blue.")
    door = input("Which colour de you choose?").lower()

    if door == "red":
      print("Burned by fire. Game Over!")
    elif door == "blue":
      print("Eaten by beasts. Game Over!")
    elif door == "yellow":
      print("You Win!")
    else: 
      print("You should choose between \"red\", \"blue\" and \"yellow\". Try again!")
  
  else: 
    print("You should choose between \"wait\" and \"swim\". Try again!")

else:
    print("You should choose between \"left\" or \"right\". Try again!")

