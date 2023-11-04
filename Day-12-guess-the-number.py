import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number = random.randint(1, 100)
print(number)
dif = input("Choose a difficulty. Type 'easy' or 'hard': ")
while dif != "easy" and dif != "hard":
    dif = input("Choose a difficulty. Type 'easy' or 'hard': ")
if dif == "easy":
    attempts = 10
else:
    attempts = 5
print(f"you have {attempts} attempts remaining to guess the number")
while attempts > 0:
    guess = int(input("Make a guess:"))
    if guess == number:
        print(f"You got it! The answer was {number}.")
        exit()
    elif guess < number:
        print("Too low")
    else:
        print("Too high")
    print("Guess again")
    attempts -= 1
    print(f"You have {attempts} attempts remaining to guess the number.")
exit()
