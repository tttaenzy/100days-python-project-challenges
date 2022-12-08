# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from replit import clear
def play_again():
  play_again=input("do you like to play again? type 'y' or 'n':")
  if play_again=='y':
    clear()
    guessing_game()
  else:
    clear()
def guessing_game():
  random_number=random.randint(1,101)
  print(random_number)
  print("welcome to number guessing game.")
  print("i am thinking of number between 1 to 100")
  level=input("choose difficulty. type 'easy' or 'hard': ")
  print("------------------------------------------------")
  if level=='easy':
    def level_easy():
        for round in range(10,0,-1):
          print(f"you have {round} chance to guess the number")
          answer=int(input("Make a guess :"))
          if answer < random_number:
            print("Too low")
          elif answer >random_number:
            print("too high")
          elif answer==random_number:
            print(f"you won!! the guess {random_number} is same as your answer{answer}")
            play_again()
            return
                
    level_easy()
  if level =='hard':
    def level_hard():
      hard=range(5,0,-1)
      for round in hard:
        print(f"you have {round} chance to guess the number")
        answer=int(input("Make a guess :"))
        if answer < random_number:
            print("Too low")
        elif answer >random_number:
            print("too high")
        elif answer==random_number:
          print(f"you won!! the guess {random_number} is same as your answer{answer}")
          play_again()
          return 
    level_hard()
guessing_game()

      





            
  #   elif level=='hard':
  #     print("you have 5 chance to guess the number ")
  # answer=input("Make a guess : ")