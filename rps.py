import tkinter as tk
import random


def choose_rock():
    global user_choice
    user_choice = "Rock"
    update_user_selection()
    check_winner()


def choose_paper():
    global user_choice
    user_choice = "Paper"
    update_user_selection()
    check_winner()


def choose_scissors():
    global user_choice
    user_choice = "Scissors"
    update_user_selection()
    check_winner()


def update_user_selection():
    global user_choice, user_choice_label
    user_choice_label.config(text=f"You chose: {user_choice}")
    # Disable buttons after user selection
    rock_button.config(state=tk.DISABLED)
    paper_button.config(state=tk.DISABLED)
    scissors_button.config(state=tk.DISABLED)


def check_winner():
    global user_choice, computer_selection, result_label

    if user_choice is None:
        return

    computer_selection = random.choice(["Rock", "Paper", "Scissors"])
    computer_choice_label.config(text=f"Computer chose: {computer_selection}")

    # Determine winner
    if user_choice == computer_selection:
        result_label.config(text="It's a tie!")
    elif (user_choice == "Rock" and computer_selection == "Scissors") or (
        user_choice == "Paper" and computer_selection == "Rock"
    ) or (user_choice == "Scissors" and computer_selection == "Paper"):
        result_label.config(text="You Win!")
    else:
        result_label.config(text="You Lose!")


def reset_game():
    global user_choice, computer_selection, rock_button, paper_button, scissors_button
    user_choice = None
    computer_selection = None
    user_choice_label.config(text="Your Choice:")
    computer_choice_label.config(text="Computer's Choice:")
    result_label.config(text="")
    # Enable buttons after reset
    rock_button.config(state=tk.NORMAL)
    paper_button.config(state=tk.NORMAL)
    scissors_button.config(state=tk.NORMAL)


# Create the main window
window = tk.Tk()
window.title("Rock Paper Scissors")

# Title label
title_label = tk.Label(window, text="Rock Paper Scissors", font=("Arial", 20))
title_label.pack(padx=10, pady=10)

# User choice label
user_choice_label = tk.Label(window, text="Your Choice:")
user_choice_label.pack()

# Computer choice label
computer_choice_label = tk.Label(window, text="Computer's Choice:")
computer_choice_label.pack()

# Result label
result_label = tk.Label(window, text="")
result_label.pack()

# Button frame
button_frame = tk.Frame(window)
button_frame.pack()

# Rock button
user_choice = None  # Global variable to track user selection
rock_button = tk.Button(button_frame, text="Rock", command=choose_rock)
rock_button.pack(side=tk.LEFT, padx=10)

# Paper button
paper_button = tk.Button(button_frame, text="Paper", command=choose_paper)
paper_button.pack(side=tk.LEFT, padx=10)

# Scissors button
scissors_button = tk.Button(button_frame, text="Scissors", command=choose_scissors)
scissors_button.pack(side=tk.LEFT, padx=10)

# Reset button
reset_button = tk.Button(window, text="Reset Game", command=reset_game)
reset_button.pack(pady=10)

# Start the main event loop
window.mainloop()
