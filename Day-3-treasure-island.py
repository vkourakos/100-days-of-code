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
in1 = input("You arrive at a crossroad. Do you want to go left or right?").lower()
if in1 == "left":
  in2= input("You keep walking until you reach a lake. YOu have to cross it! Will you wait for a boat or will you swim ? (wait / swim)").lower()
  if in2 == "wait":
    in3 = input("The boat arrived and you got across to the other side where you see three doors, a yellow one, a blue one and a red one. Which one will you open? (yellow / blue / red)").lower()
    if in3 == "yellow":
      print("You Win!")
    elif in3 == "red":
      print("It was a trap! Game Over!")
    elif in3 == "blue": 
      print("You see the treasure inside! You get closer just to realise that the coins are made of chocolate. Game Over!")
    else: 
      print("Game Over")
  else:
    print("you had almost reached the other side when a shark attacked you! Game Over!")
else:
  print("You walked right into a lava pit. Game Over!")
  
