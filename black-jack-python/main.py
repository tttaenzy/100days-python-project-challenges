############### Blackjack Project #####################
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
import random
from replit import clear
from art import logo

def black_jack_game():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  
  def calculate_score(list):
    if sum(cards)==21 and len(cards)==2:
      return 0
    elif 11 in cards and sum(cards)>21:
      cards.remove(11)
      cards.append(1)
    return sum(list)
  #Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
  #user_cards = []
  #computer_cards = []
  user_cards=[]
  computer_cards=[]
  is_game_over=False

  def play_again():
    restart_game=input("do you want to restart the game. type 'y' or 'n'")
    if restart_game=='y':
      clear()
      print(logo)
      black_jack_game()

  def compare(user_score,computer_score):
      if computer_score==user_score:
        print(computer_score)
        return "DRAW"
      elif computer_score==0:
        print(computer_score)
        return "computer has blackJack, Computer win"
      elif user_score==0:
        return "user has blackJack, User win"
      elif user_score > 21:
        print("User Lost")
        return play_again()
      elif computer_score>21:
        print(computer_score)
        return "Computer Lost"
      elif user_score>computer_score:
        return "User win"
      else:
        print(computer_score)
        return "computer win"
  # to generate random number from cards list
  def deal_card():
    return random.choice(cards)
  # random user and computer deal twice
  
  # to execute random number two times and put it in user and computer cards
  for _ in range(2):
    user_random=random.choice(cards)
    user_cards.append(user_random)
    computer_random=random.choice(cards)
    computer_cards.append(computer_random)
  
  while not is_game_over:
    user_score=calculate_score(user_cards)
    computer_score=calculate_score(computer_cards)
    print(f"user cards are {user_cards} and current score is {user_score}")
    print(f"computer cards are {computer_cards[0]}")
    #Hint 6: Create a function called calculate_score() that takes a List of cards as input 
    #and returns the score. 
    #Look up the sum() function to help you do this.
    
    #Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
    
    #Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
    
    #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    
    #Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
    if user_score==0 or computer_score ==0 or user_score>21:
      is_game_over=True
    else:
      another=input("do you like to draw another card? type 'y' or 'n': ")
      if another=='y':
        user_cards.append(deal_card())
      else:
        is_game_over=True
  #Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
  
  #Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
  while computer_score!=0 and computer_score<17:
    computer_cards.append(deal_card())
    computer_score=calculate_score(computer_cards)
  print(f"user cards are {user_cards} and user current score is {user_score}")
  print(f"computer cards are {computer_cards} and computer current score is {computer_score}")
  print(compare(user_score,computer_score))

  play_again()
  #Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
 

black_jack_game()


#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

