from replit import clear
from art import logo

print(logo)
bids = {}
next = True
while next:
    clear()
    name = input("What is your name?:")
    bid = int(input("What is your bid?: $"))
    bids[name] = bid
    answer = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if answer == "no":
        next = False
    elif answer == "yes":
        clear()

max_bid = 0
max_bidder = ""

for key in bids:
    if bids[key] > max_bid:
        max_bid = bids[key]
        max_bidder = key

print(f"The Winner is {max_bidder} with a bid of ${max_bid}")
