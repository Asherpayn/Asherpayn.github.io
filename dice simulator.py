import tkinter as tk
import random

def roll_dice():
    return random.randint(1, 6)

def roll_button_click():
    result = roll_dice()
    result_label.config(text=f"You rolled a {result}!")

# Create the main application window
app = tk.Tk()
app.title("Dice Simulator")

# Create a button to roll the dice
roll_button = tk.Button(app, text="Roll the Dice", command=roll_button_click)
roll_button.pack(pady=10)

# Create a label to display the result
result_label = tk.Label(app, text="", font=("Helvetica", 16))
result_label.pack()

# Run the application
app.mainloop()