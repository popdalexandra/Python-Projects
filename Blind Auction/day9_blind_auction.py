from day9_art import logo
print(logo)

bid_dict = {}

def the_winner (bidding_record):
    high_value = 0
    winner = ""
    for bidder in bidding_record:
        value = int(bidding_record[bidder])
        if value > high_value:
            high_value = value
            winner = bidder
    print(f"The winner is {winner} with a bid of ${high_value}")

def clear(): # Print 50 blank lines
    print("\n" * 50)

stop_the_bid = False

while not stop_the_bid:
    name = input("What is your name? ")
    bid = input("What is your bid? $")
    bid_dict[name] = bid

    continue_bidding = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    if continue_bidding == "no":
        stop_the_bid = True
        clear()
        the_winner(bid_dict)
    elif continue_bidding == "yes":
        clear()
    
        
