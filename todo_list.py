from tkinter import *
from tkinter import messagebox

# Initialize window
root = Tk()
root.title("To-Do List")
root.geometry("400x500")
root.configure(bg="#EAEAEA")  # Light Grey Background

# Task List
tasks = []

# Functions
def add_task():
    task = task_entry.get().strip()
    if task:
        tasks.append(task)
        update_listbox()
        task_entry.delete(0, END)
        messagebox.showinfo("Success", "Task Added Successfully!")
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def update_task():
    try:
        selected_index = task_listbox.curselection()[0]
        new_task = task_entry.get().strip()
        if new_task:
            tasks[selected_index] = new_task
            update_listbox()
            task_entry.delete(0, END)
            messagebox.showinfo("Success", "Task Updated Successfully!")
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")
    except IndexError:
        messagebox.showerror("Error", "Please select a task to update.")

def delete_task():
    try:
        selected_index = task_listbox.curselection()[0]
        tasks.pop(selected_index)
        update_listbox()
        messagebox.showinfo("Success", "Task Deleted Successfully!")
    except IndexError:
        messagebox.showerror("Error", "Please select a task to delete.")

def update_listbox():
    task_listbox.delete(0, END)
    for i, task in enumerate(tasks, 1):
        task_listbox.insert(END, f"{i}. {task}")

# UI Components
Label(root, text="To-Do List Application", font=("Helvetica", 16), bg="#EAEAEA", fg="#000000").pack(pady=10)

task_entry = Entry(root, width=30, font=("Arial", 12), bg="#FFFFFF", fg="#000000", insertbackground="black")
task_entry.pack(pady=5)

button_frame = Frame(root, bg="#EAEAEA")
button_frame.pack(pady=10)

add_button = Button(button_frame, text="Add Task", command=add_task, bg="#B7E4C7", fg="#000000", width=10)
add_button.grid(row=0, column=0, padx=5)

update_button = Button(button_frame, text="Update Task", command=update_task, bg="#FFE082", fg="#000000", width=10)
update_button.grid(row=0, column=1, padx=5)

delete_button = Button(button_frame, text="Delete Task", command=delete_task, bg="#FF8A80", fg="#000000", width=10)
delete_button.grid(row=0, column=2, padx=5)

task_listbox = Listbox(root, selectmode=SINGLE, width=40, height=10, font=("Arial", 12), bg="#FFFFFF", fg="#000000", bd=1, highlightthickness=0)
task_listbox.pack(pady=10)

root.mainloop()
