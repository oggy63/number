#Number guessing game
#James Kilpatrick
#ec1929115

import random

while True:
  # Generate a random number between 1 and 10
  secret_num = random.randint(1, 10)

  # Initialize a variable to track whether the player has won
  won = False

  # Get the player's guess
  guess = int(input("Enter a number between 1 and 10: "))

  # Keep asking the player for a guess until they win or choose to stop
  while not won:
    if guess == secret_num:
      print("You guessed the correct number! You win!")
      won = True
    elif guess < secret_num:
      print("Your guess is too low. Try again.")
      guess = int(input("Enter a number between 1 and 10: "))
    else:
      print("Your guess is too high. Try again.")
      guess = int(input("Enter a number between 1 and 10: "))
  
  # Ask the player if they want to play again
  play_again = input("Do you want to play again? (y/n) ")
  if play_again.lower() != 'y':
    break

print("Thank you for playing!")
