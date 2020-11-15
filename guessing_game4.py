import random


def user_input():
  while True:
    try:
      user_attempt = int(input("Pick a number between 1 and 10: "))
      while user_attempt > 10 or user_attempt < 1:
        user_attempt = int(input("\nInvalid entry outside of the range. \n\nEnter a number between 1 and 10: "))
      return user_attempt
    except ValueError:
      print("Oh no! That's not a valid value. Try again...")


def start_game():
  print("""
  -----------------------------------------
  Hello welcome to the number guessing game
  -----------------------------------------
  """)
  random_number = random.randrange(1,11)
  attempts = 1
  user_attempt = user_input()
  
  while user_attempt != random_number:
      if user_attempt > random_number:
        attempts += 1
        print("It is lower.")
        user_attempt = user_input()
        
      elif user_attempt < random_number:
        attempts += 1
        print("It is higher.")
        user_attempt = user_input()
        
      else:
        break
        attempts += 1
  print("Got it! it took you {} attempts.".format(attempts))
  
  play_again = input("Game Over! Would you like to play again Yes/No: ")
  if play_again.lower() == 'yes':
    start_game()
  else:
    print("Thank you for playing, Goodbye!")
      
start_game()