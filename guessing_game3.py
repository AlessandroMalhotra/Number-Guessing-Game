import random

def start_game():
  print("""
  -----------------------------------------
  Hello welcome to the number guessing game
  -----------------------------------------
  """)
  random_number = random.randrange(1,11)
  attempts = 1
  try:
    user_attempt = int(input("Pick a number between 1 and 10: "))
  except ValueError:
    print("Oh no! That's not a valid value. Try again...")
  else:
    while user_attempt != random_number:
    
      if user_attempt > random_number:
        attempts += 1
        print("It is lower.")
        user_attempt = int(input("Pick a number between 1 and 10: "))
        
      elif user_attempt < random_number:
        attempts += 1
        print("It is higher.")
        user_attempt = int(input("Pick a number between 1 and 10: "))
        
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