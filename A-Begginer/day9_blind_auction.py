from day9_art import logo
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def find_highest_bid(bid_record):
    highest_bid = 0
    winner = ""
    for bidder in bid_record:
        bid_amount = bid_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


print(logo)

bids = {}
end_auction = False

while not end_auction:
    name = input("What is your name?\n")
    bid = int(input("What is your bid?\n"))

    bids[name] = bid

    should_continue = input("Are there any other bidders? Type yes or no:\n")
    if should_continue == "no":
        end_auction = True
    cls()

find_highest_bid(bids)
