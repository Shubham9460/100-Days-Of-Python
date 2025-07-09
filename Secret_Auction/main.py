import logo
print(logo.logo1)
def find_highest_bedder(bidding_dictionary):
    highest_amount = 0
    winner = " "
    for bidder in bidding_dictionary:
        bidding_amount = bidding_dictionary[bidder]
        if bidding_amount > highest_amount:
            highest_amount = bidding_amount
            winner = bidder

    print(f"winner is {winner} and amount is {highest_amount}")

bids = {}
continues = True
while continues:
    name = input("What is your name : ")
    price = int(input("what is your bid : $"))
    bids[name] = price
    should_continue = input("Are there any other bidder ? type 'yes' or 'no' .\n").lower()
    if should_continue == "no":
        find_highest_bedder(bids)
        continues = False
    elif should_continue == "yes":
        print("\n" * 20)





