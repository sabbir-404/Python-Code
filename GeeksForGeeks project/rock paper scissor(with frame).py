import random
import tkinter as tk
from tkinter import messagebox

def play(user_choice):
    choices = ['rock', 'paper', 'scissors']
    cmp_choice = random.choice(choices)

    if user_choice == cmp_choice:
        result = "It's a tie!"
    elif (user_choice == 'rock' and cmp_choice == 'scissors') or \
         (user_choice == 'paper' and cmp_choice == 'rock') or \
         (user_choice == 'scissors' and cmp_choice == 'paper'):
        result = "You win this round!"
        global usr_point
        usr_point += 1
    else:
        result = "Computer wins this round!"
        global cmp_point
        cmp_point += 1

    result_label.config(text=f"Your choice: {user_choice}\nComputer's choice: {cmp_choice}\n{result}")

    rounds_remaining.set(rounds_remaining.get() - 1)
    if rounds_remaining.get() == 0:
        if usr_point == 3:
            final_result = 'Congratulations, you WIN!!!'
        else:
            final_result = 'Sorry, you lose.'

        messagebox.showinfo("Game Over", f"Final score - You: {usr_point}, Computer: {cmp_point}\n{final_result}")
        reset_game()

def reset_game():
    global usr_point, cmp_point
    usr_point = 0
    cmp_point = 0
    rounds_remaining.set(3)
    result_label.config(text="")

usr_point = 0
cmp_point = 0

root = tk.Tk()
root.title("Rock Paper Scissors Game")

rounds_remaining = tk.IntVar(value=3)

instructions = tk.Label(root, text='Winning rules of the game ROCK PAPER SCISSORS are:\n'
                                   'Rock vs Paper -> Paper wins\n'
                                   'Rock vs Scissors -> Rock wins\n'
                                   'Paper vs Scissors -> Scissors wins\n\n'
                                   'You have 3 chances, if you win all 3 times you will be the winner.\n'
                                   'Please select one of the following choices:')
instructions.pack()

button_frame = tk.Frame(root)
button_frame.pack()

rock_button = tk.Button(button_frame, text="Rock", command=lambda: play('rock'))
rock_button.grid(row=0, column=0, padx=10, pady=10)

paper_button = tk.Button(button_frame, text="Paper", command=lambda: play('paper'))
paper_button.grid(row=0, column=1, padx=10, pady=10)

scissors_button = tk.Button(button_frame, text="Scissors", command=lambda: play('scissors'))
scissors_button.grid(row=0, column=2, padx=10, pady=10)

result_label = tk.Label(root, text="")
result_label.pack()

rounds_label = tk.Label(root, textvariable=rounds_remaining)
rounds_label.pack()

reset_button = tk.Button(root, text="Reset Game", command=reset_game)
reset_button.pack()

root.mainloop()
