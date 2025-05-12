import random

print('Winning rules of the game ROCK PAPER SCISSORS are :\n'
    + "Rock vs Paper -> Paper wins \n"
    + "Rock vs Scissors -> Rock wins \n"
    + "Paper vs Scissors -> Scissors wins \n")

print("You have 3 chances, if you win all 3 times you will be the winner.\n\nPlease enter number from the following choices:-\n1. Rock\n2. Paper\n3. Scissors")

usr_point = 0
cmp_point = 0
choices = ['rock', 'paper', 'scissors']
rounds = 3

while rounds > 0:
    cmp_choice = random.choice(choices)
    
    while True:
        usr = int(input("\nEnter your choice (1 for Rock, 2 for Paper, 3 for Scissors): "))
        if usr in [1, 2, 3]:
            break
        else:
            print("\nInvalid choice, please choose a number between 1 and 3.")

    if usr == 1:
        usr_choice = 'rock'
    elif usr == 2:
        usr_choice = 'paper'
    elif usr == 3:
        usr_choice = 'scissors'
    
    print(f"\nYour choice: {usr_choice}")
    print(f"Computer's choice: {cmp_choice}")
    
    if usr_choice == cmp_choice:
        print("It's a tie!")
    elif (usr_choice == 'rock' and cmp_choice == 'scissors') or (usr_choice == 'paper' and cmp_choice == 'rock') or (usr_choice == 'scissors' and cmp_choice == 'paper'):
        print("You win this round!")
        usr_point += 1
    else:
        print("Computer wins this round!")
        cmp_point += 1

    rounds -= 1

print(f"\nFinal score - You: {usr_point}, Computer: {cmp_point}")
if usr_point > cmp_point:
    print('\nCongratulations, you WIN!!!')
else:
    print('\nSorry, you lose.')

k = input("\nPress ENTER to close.")