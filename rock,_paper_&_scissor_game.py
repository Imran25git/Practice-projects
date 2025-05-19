# Rock Pper Scissor Game 

import random

rock = 0
paper = 1
scissor = 2
l1 = [rock, paper, scissor]

# Initialize scores
my_score = 0
comp_score = 0

while my_score < 30 and comp_score < 30:
    my_turn = int(input("Enter your turn (0 for Rock, 1 for Paper, 2 for Scissors): "))
    if my_turn not in l1:
        print("Invalid choice, try again.")
        continue

    computer_turn = random.choice(l1)
    print(f"Computer's turn: {computer_turn}")

    if my_turn == computer_turn:
        print("Tie! No points awarded.")
    elif my_turn == rock and computer_turn == paper:
        print("Computer gets 5 points")
        comp_score += 5
    elif my_turn == rock and computer_turn == scissor:
        print("You get 5 points")
        my_score += 5
    elif my_turn == paper and computer_turn == rock:
        print("You get 5 points")
        my_score += 5
    elif my_turn == paper and computer_turn == scissor:
        print("Computer gets 5 points")
        comp_score += 5
    elif my_turn == scissor and computer_turn == rock:
        print("Computer gets 5 points")
        comp_score += 5
    elif my_turn == scissor and computer_turn == paper:
        print("You get 5 points")
        my_score += 5

    print(f"Your score: {my_score}, Computer's score: {comp_score}")

# Announce the winner
if my_score >= 30:
    print("Congrats! You Win!")
else:
    print("You Lose! Computer Wins!")
