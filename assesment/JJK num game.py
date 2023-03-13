import random

numbers = [1,2,3,4,5,6]
continuePlaying = "True"
score = 0

while continuePlaying == "True":
  randomNumber = random.choice(numbers)
  
  userNumber = int(input("Please enter a number between 1 and 6: "))
  
  if userNumber == randomNumber:
    continuePlaying = "false"
  else:
    print("Well done you avoided the random number: ")  
    score = score + 1
print("Game over you have scored", score, "Points: ")    
  