import tkinter as tk
from tkinter import messagebox
import random

# Create card pairs
cards = ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D',
         'E', 'E', 'F', 'F', 'G', 'G', 'H', 'H']
random.shuffle(cards)

buttons = []
first_card = None
second_card = None
lock = False
matched = 0

# Function to handle card click
def flip_card(index):
    global first_card, second_card, lock, matched

    if lock:
        return

    if buttons[index]["text"] != "":
        return

    buttons[index]["text"] = cards[index]

    if first_card is None:
        first_card = index
    elif second_card is None:
        second_card = index
        lock = True
        root.after(800, check_match)

# Function to check for match
def check_match():
    global first_card, second_card, lock, matched

    if cards[first_card] == cards[second_card]:
        buttons[first_card]["state"] = "disabled"
        buttons[second_card]["state"] = "disabled"
        matched += 2

        if matched == len(cards):
            messagebox.showinfo("Congratulations!", "You matched all the cards!")

    else:
        buttons[first_card]["text"] = ""
        buttons[second_card]["text"] = ""

    first_card = None
    second_card = None
    lock = False

# Create main window
root = tk.Tk()
root.title("Memory Card Matching Game")

# Create buttons
for i in range(16):
    btn = tk.Button(root,
                    text="",
                    width=8,
                    height=4,
                    font=("Arial", 14),
                    command=lambda i=i: flip_card(i))
    btn.grid(row=i//4, column=i%4, padx=5, pady=5)
    buttons.append(btn)

root.mainloop()