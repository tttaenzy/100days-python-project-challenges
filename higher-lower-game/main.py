from random import choice
from game_data import data
from art import logo,vs
from replit import clear

score=0
# function to check answer
def check(guess, a_follower,b_follower):
  if a_follower > b_follower:
    return guess=='a' or guess=='A'
  else:
    return guess=='b' or guess=='B'

# formate function is used to retrieve data from dict in list.and to use repeately for both A and b account
def format_account(account):
  name=account["name"]
  description=account["description"]
  follower=account["follower_count"]
  country=account["country"]
  return f"{name} a {description} from {country}"
print(logo)
is_game_should_continue=True
accountB=choice(data)
while is_game_should_continue: 
  accountA=accountB
  accountB=choice(data)
  while accountA==accountB:
    accountB=choice(data)
    
  print(f"Compare A: {format_account(accountA)}")
  print(vs)
  print(f"Against B: {format_account(accountB)}")
  guess=input("Who has more follower? 'A' or 'B': ")
  a_follower=accountA["follower_count"]
  b_follower=accountB["follower_count"]
  
  is_correct=check(guess,a_follower,b_follower)
  if is_correct:
    score+=1
    print(f"you are right and your current score is {score}")
    clear()
    print(f"Current score {score}")
  else:
    is_game_should_continue=False
    print(f"sorry you are wrong and your current score is {score} ")