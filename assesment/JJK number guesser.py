import random

# Initialize a variable to keep track of the player's score
score = 0

# Set the win state
#When game reaches 15 point you win
win_points = 15

play_again = "Y"

# Start the game
while play_again == "Y":
    # Choose a random number from a list of numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = random.choice(numbers)
    
    # Get a guess from the player
    guess = int(input("Please enter a number between 1 and 10: "))
    
    # If the guess is correct, break out of the looP
    if guess == target:
         play_again = "N"   
    else:
      print("Well done you won: ")
          
        # Otherwise, increment the score
      score += 1  

    # Check if the player has reached the win state
    if score >= win_points:
        print("Congratulations, you reached the max score!")
        break
      # Print the player's score and ask if they want to play again
print("Your score is", score)      
    
