#Name : BothMind Game
#Author : Ahum Maitra
# Date : 18.06.2025




from tkinter import *
import random

Window = Tk()
Window.geometry("790x900")
Window.title("BothMind")
Window.configure(bg="#4E0082")

# Header
Locky_header_text = Label(
    Window,
    text="Welcome to Bothmind",
    font=("Arial", 24, "bold"),
    bg="purple",
    fg="white",
    pady=20,
)
Locky_header_text.pack(pady=30)

# Entry label and input
Main_text = Label(Window, text="Enter your secret code (3-digit number):", font=("Arial", 20, "bold"), bg="#4E0082", fg="white")
Main_text.pack(pady=40)

Main_entry = Entry(Window, font=("Arial", 16), width=20)
Main_entry.pack(pady=10)

# Output label to show guesses
guess_label = Label(Window, text="", font=("Arial", 16), bg="white", width=40, pady=10)
guess_label.pack(pady=20)

# Error label
error_label = Label(Window, text="", font=("Arial", 12), fg="red", bg="#4E0082")
error_label.pack()

# Win message label
win_label = Label(Window, text="", font=("Arial", 18, "bold"), fg="yellow", bg="#4E0082")
win_label.pack(pady=10)

# Main function
def start_guessing():
    try:
        user_input = int(Main_entry.get())

        # Validate 3-digit number
        if user_input < 100 or user_input > 999:
            error_label.config(text="Please enter a 3-digit number!")
            return
        else:
            error_label.config(text="")  # clear error

        # Computer makes a guess
        guess = random.randint(100, user_input)  # To match 3-digit logic
        guess_label.config(text=f"Computer guessed: {guess}")

        # Match check
        if user_input == guess:
            win_label.config(text="Your and computer mind matched!")
        else:
            win_label.config(text="Try again!")

    except ValueError:
        error_label.config(text="Invalid input! Please enter a number.")

# Start button
submit_button = Button(
    Window,
    text="Start Guessing",
    font=("Arial", 16, "bold"),
    bg="purple",
    fg="white",
    command=start_guessing,
)
submit_button.pack(pady=10)

# Stop function
def stop_game():
    Main_entry.delete(0, END)
    guess_label.config(text="")
    error_label.config(text="")
    win_label.config(text="Game stopped.")

# Stop button
stop_button = Button(
    Window,
    text="Stop",
    font=("Arial", 14, "bold"),
    bg="red",
    fg="white",
    command=stop_game,
)
stop_button.pack(pady=10)

Window.mainloop()
