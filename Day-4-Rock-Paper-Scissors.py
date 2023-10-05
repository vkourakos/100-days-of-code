import random
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

moves = [rock, paper, scissors]
players_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0,2)
print(moves[players_choice])
print("Computer choice:")
print(moves[computer_choice])

if players_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and players_choice == 2:
  print("You lose")
elif computer_choice > players_choice:
  print("You lose")
elif players_choice > computer_choice:
  print("You win!")
elif computer_choice == players_choice:
  print("It's a draw")
  
