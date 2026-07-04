import tkinter as tk
from tkinter import messagebox
import random

root = tk.Tk()
root.title("Puzzle Rearrangement Game")

# Goal arrangement
goal = [1, 2, 3,
        4, 5, 6,
        7, 8, ""]

# Shuffle puzzle
puzzle = goal[:]
while True:
    random.shuffle(puzzle)
    if puzzle != goal:
        break

buttons = []

# Update button text
def update_board():
    for i in range(9):
        buttons[i]["text"] = puzzle[i]

# Check if puzzle is solved
def check_win():
    if puzzle == goal:
        messagebox.showinfo("Congratulations!", "Puzzle Solved!")

# Move tile
def move(index):
    empty = puzzle.index("")

    # Valid moves
    valid = []

    if empty % 3 != 0:
        valid.append(empty - 1)
    if empty % 3 != 2:
        valid.append(empty + 1)
    if empty > 2:
        valid.append(empty - 3)
    if empty < 6:
        valid.append(empty + 3)

    if index in valid:
        puzzle[empty], puzzle[index] = puzzle[index], puzzle[empty]
        update_board()
        check_win()

# Create buttons
for i in range(9):
    btn = tk.Button(root,
                    width=6,
                    height=3,
                    font=("Arial", 18),
                    command=lambda i=i: move(i))
    btn.grid(row=i//3, column=i%3, padx=2, pady=2)
    buttons.append(btn)

update_board()

root.mainloop()