import tkinter as tk
from tkinter import messagebox

# Animal data (Replace image filenames with your own)
animals = [
    ("lion.png", "Lion", ["Lion", "Tiger", "Cat", "Dog"]),
    ("elephant.png", "Elephant", ["Elephant", "Horse", "Cow", "Buffalo"]),
    ("tiger.png", "Tiger", ["Leopard", "Tiger", "Lion", "Fox"]),
    ("zebra.png", "Zebra", ["Horse", "Donkey", "Zebra", "Deer"])
]

score = 0
current = 0

# Check answer
def check_answer(choice):
    global score, current

    if choice == animals[current][1]:
        score += 1

    current += 1

    if current < len(animals):
        load_question()
    else:
        messagebox.showinfo(
            "Game Over",
            f"Final Score: {score}/{len(animals)}"
        )
        root.destroy()

# Load question
def load_question():
    img = tk.PhotoImage(file=animals[current][0])
    image_label.config(image=img)
    image_label.image = img

    options = animals[current][2]

    btn1.config(text=options[0],
                command=lambda: check_answer(options[0]))
    btn2.config(text=options[1],
                command=lambda: check_answer(options[1]))
    btn3.config(text=options[2],
                command=lambda: check_answer(options[2]))
    btn4.config(text=options[3],
                command=lambda: check_answer(options[3]))

    score_label.config(text=f"Score: {score}")

# GUI
root = tk.Tk()
root.title("Animal Identification Game")

score_label = tk.Label(root, text="Score: 0",
                       font=("Arial", 14))
score_label.pack(pady=10)

image_label = tk.Label(root)
image_label.pack(pady=10)

btn1 = tk.Button(root, width=20)
btn1.pack(pady=5)

btn2 = tk.Button(root, width=20)
btn2.pack(pady=5)

btn3 = tk.Button(root, width=20)
btn3.pack(pady=5)

btn4 = tk.Button(root, width=20)
btn4.pack(pady=5)

load_question()

root.mainloop()