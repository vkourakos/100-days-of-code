import art
import random
from replit import clear
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
play = True
def get_user_score(hand):
    return sum(hand)

def get_computer_score(hand):
    return sum(hand)

def result():
    if user_lost:
        print("You went over. You lose")    
    elif computer_lost:
        print("Opponent went over. You win")
    elif user_score == computer_score:
        print("Draw")
    elif user_score > computer_score and user_score == 21:
        print("Win with a Blackjack")
    elif computer_score > user_score and computer_score == 21: 
        print("You lose. Opponent has a Blackjack")
    elif user_score > computer_score:
        print("You Win!")
    else:
        print("You Lose!")

while play:
    user_hand= []
    computer_hand = []
    user_score = 0
    computer_score = 0
    answer = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    clear()
    if answer == "y":
        print(art.logo)
        for i in range(2):
            user_hand.append(random.randint(2,11))
            if get_user_score(user_hand) > 21:
                user_hand[user_hand.index(11)] = 1
        computer_hand.append(random.randint(2,11))
        user_score = get_user_score(user_hand)
        computer_score = get_computer_score(computer_hand)
        another = True
        user_lost = False
        while another:
            print(f"Your cards: {user_hand}, current score: {user_score}")
            print(f"Computer's first card: {computer_score}")
            answer2 = input("Type 'y' to get another card, type 'n' to pass: ")
            if answer2 == "y" and not user_lost:
                user_hand.append(random.randint(2,11))
                if get_user_score(user_hand) > 21:
                    if 11 in user_hand:
                        user_hand[user_hand.index(11)] = 1
                    else:
                        user_lost = True
                        another = False
                user_score = get_user_score(user_hand)
            elif answer2 != "y":
                another = False
        computer_pull = True
        computer_lost = False
        while computer_pull:
            computer_hand.append(random.randint(2,11))
            computer_score = get_computer_score(computer_hand)
            if get_computer_score(computer_hand) > 21:
                if 11 in computer_hand:
                    computer_hand[computer_hand.index(11)] = 1
                    computer_score = get_computer_score(computer_hand)
                else:
                    computer_lost = True
                    computer_pull = False
            elif get_computer_score(computer_hand) > 17:
                print(">17")
                computer_pull = False
        print(f"Your final hand: {user_hand}, final score: {user_score}")
        print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")
        result()
    else:
        play = False
