# Number Guessing Game

import random
n = random.randint(1,100)
a = -1
guess = 0
print("Guess the number between 1 to 100")
while(a != n):
  guess +=1
  a = int(input("Enter the guess number: "))
  if(a<n or a>100):
    print("You had guessed wrong number. Read intructions again")
  elif(a>n):
    print("Lower number please")
  else:
    print("Higher number please")

print(f"You has correctly guess {n} numbers in {guess} attempts")
