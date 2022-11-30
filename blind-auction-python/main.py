from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
# print(logo)
bidding_list={}
def starting():
  name=input("what is your name:")
  bid=int(input("what is your bid: $"))
  bidding_list[name]=bid
  compititor=input("is there any person who wants to bid too? yes/no \n")
  if compititor=='yes':
    clear()
    starting()
  else:
    highest_bid=0
    winner=""
    for bidder in bidding_list:
      bid_amount=bidding_list[bidder]
      if bid_amount>highest_bid:
        highest_bid=bid_amount
        winner=bidder
    print(f"winner is {winner} with bid of ${highest_bid}")
    

starting()
# name=input("what is your name:")
# bid=input("what is your bid: $")

# bidding_list[name]=bid


  
  

