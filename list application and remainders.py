from tkinter import *
root = Tk()
root.title("To-Do List")
root.geometry("300x400")
tasks = []
#add task
def add_task():
    task = entry.get()
    if task != "":
        tasks.append(task)
        listbox.insert(END, task)
        entry.delete(0, END)
#delete selected task
def delete_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        listbox.delete(index)
        tasks.pop(index)
#clear all tasks
def clear_tasks():
    listbox.delete(0, END)
    tasks.clear()
#entry box
entry = Entry(root, width=25)
entry.pack(pady=10)
#buttons
Button(root, text="Add Task", command=add_task).pack(pady=5)
Button(root, text="Delete Task", command=delete_task).pack(pady=5)
Button(root, text="Clear Tasks", command=clear_tasks).pack(pady=5)
#listbox
listbox = Listbox(root, width=35, height=12)
listbox.pack(pady=10)
root.mainloop()