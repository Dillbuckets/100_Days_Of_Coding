import day9_blind_auction_art
import os

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for contestant in bidding_record:
        bid_amount = bidding_record[contestant]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = contestant
    print(f"The winnner is {winner} with a bid of ${highest_bid}")

print(day9_blind_auction_art.logo)
auction_over = False
bids = {}
while auction_over == False:
    name = input("What is you name?: ")
    bid = int(input("What is your bid?: $"))
    bids[name] = bid
    repeat = input("Are there more bidders? Type \"yes\" or \"no\": ").lower()
    if repeat == "no":
        auction_over = True
        os.system('clear')
        find_highest_bidder(bids)
    elif repeat == "yes":
        os.system('clear')