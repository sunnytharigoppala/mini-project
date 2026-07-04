from tkinter import *
root = Tk()
root.title("Draw with Mouse")
canvas = Canvas(root, width=500, height=400,bg="white")
canvas.pack()
#function to draw when mouse moves
def draw(event):
    x, y = event.x, event.y
    canvas.create_oval(x, y, x+3, y+3, fill="black", outline="black")
#blind mouse movement with left button pressed
canvas.bind("<B1-Motion>",draw)
root.mainloop()
