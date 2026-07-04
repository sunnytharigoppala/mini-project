from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Attendance Management System")
root.geometry("500x400")
attendance = {}
#add student
def add_student():
    name = entry.get()
    if name != "":
        attendance[name] = "Absent"
        tree.insert("",END, values=(name,"Absent"))
        entry.delete(0, END)
#mark attendance
def mark_present():
    selected = tree.selection()
    if selected:
        item = selected[0]
        name = tree.item(item)["values"][0]
        attendance[name] = "Present"
        tree.item(item, values=(name,"Present"))
#entry
Label(root, text="Student Name").pack(pady=5)
entry = Entry(root, width=30)
entry.pack()
Button(root, text="Add Student", command=add_student).pack(pady=5)
Button(root, text="Mark Present", command=mark_present).pack(pady=5)
#table
tree = ttk.Treeview(root, columns=("Name","Attendance"), show="headings")
tree.heading("Name", text="Student Name")
tree.heading("Attendance", text="Attendance")
tree.pack(fill=BOTH, expand=True, pady=10)
root.mainloop()