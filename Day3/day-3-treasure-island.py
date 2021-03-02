###################################
#
# 100 Days of code bootcamp 2021
# (Udemy course by Angela Yu)
# 
# Day 3 project - Christopher Hagan
#
###################################

print("""
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"'"-._ ".   |
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
Welcome to Treasure Island.
Your mission is to fine the treasure.""")

gameover = False
if (input('You come to a crossroads, would you like to go left or right? ').lower().startswith('l')):
    print('You went left...')

    if (input('You arrived at a pier, you can see the island, do you wish to swim or wait for a boat? ').lower().startswith('w')):
        print('You decided to wait for a boat...')

        if(input('On the island you are greet with three doors, a Red door, a Blue door and a Yellow door, which door will you enter? ').lower().startswith('y')):
            print('You have selected the yellow door and found the treasure!')
        
        else:
            print('You have chosen poorly...')
            gameover = True
    
    else:
        gameover = True

else:
    gameover = True

if gameover:
    print('You died, sucks to be you...')
