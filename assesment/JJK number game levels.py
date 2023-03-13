import random

while True:
  # Initialize variables to track the score and the range of numbers
  score = 0
  low = 1
  high = 100

  # Ask the player for the difficulty level
  difficulty = input("Enter difficulty level (easy, medium, hard): ")

  # Set the range of numbers based on the difficulty level
  if difficulty.lower() == "easy":
    high = 50
  elif difficulty.lower() == "medium":
    high = 75
  elif difficulty.lower() == "hard":
    high = 100
  else:
    print("Invalid difficulty level. Setting difficulty to medium.")
    high = 75

  # Generate a random number between low and high
  secret_num = random.randint(low, high)

  # Get the player's first guess
  guess = int(input(f"Enter a number between {low} and {high}: "))
  score += 1

  # Keep asking the player for guesses until they guess the correct number
  while guess != secret_num:
    if guess < secret_num:
      print("Your guess is too low. Try again.")
    else:
      print("Your guess is too high. Try again.")
    guess = int(input(f"Enter a number between {low} and {high}: "))
    score += 1
  
  # Print the player's score
  print(f"You guessed the correct number in {score} tries! You win!")

  # Ask the player if they want to play again
  play_again = input("Do you want to play again? (y/n) ")
  if play_again.lower() != 'y':
    break

print("Thank you for playing!")

