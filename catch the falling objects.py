import tkinter as tk
import random

# Window
root = tk.Tk()
root.title("Catch the Falling Objects")

WIDTH = 400
HEIGHT = 500

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="lightblue")
canvas.pack()

# Basket
basket = canvas.create_rectangle(150, 460, 250, 480, fill="brown")

# Falling object
object_size = 30
obj = canvas.create_oval(180, 20, 210, 50, fill="red")

score = 0
score_text = canvas.create_text(60, 20, text="Score: 0",
                                font=("Arial", 14), fill="black")

# Move basket
def move_left(event):
    x1, y1, x2, y2 = canvas.coords(basket)
    if x1 > 0:
        canvas.move(basket, -20, 0)

def move_right(event):
    x1, y1, x2, y2 = canvas.coords(basket)
    if x2 < WIDTH:
        canvas.move(basket, 20, 0)

root.bind("<Left>", move_left)
root.bind("<Right>", move_right)

# Animate falling object
def fall():
    global score

    canvas.move(obj, 0, 5)

    ox1, oy1, ox2, oy2 = canvas.coords(obj)
    bx1, by1, bx2, by2 = canvas.coords(basket)

    # Catch
    if oy2 >= by1 and ox2 >= bx1 and ox1 <= bx2:
        score += 1
        canvas.itemconfig(score_text, text=f"Score: {score}")

        new_x = random.randint(20, WIDTH - 50)
        canvas.coords(obj, new_x, 20, new_x + object_size, 20 + object_size)

    # Miss
    elif oy2 > HEIGHT:
        new_x = random.randint(20, WIDTH - 50)
        canvas.coords(obj, new_x, 20, new_x + object_size, 20 + object_size)

    root.after(30, fall)

fall()

root.mainloop()