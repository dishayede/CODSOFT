import tkinter as tk
from tkinter import messagebox

def add_task():
    """Fetches text from the entry box and adds it to the listbox."""
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END) # Clear the input box after adding
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    """Deletes the selected task from the listbox."""
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def clear_tasks():
    """Clears all tasks from the listbox."""
    task_listbox.delete(0, tk.END)

# --- Main Window Setup ---
root = tk.Tk()
root.title("Real-Type To-Do List")
root.geometry("400x480")
root.config(bg="#f4f4f9") # Light grey background

# --- UI Elements ---
# App Title
title_label = tk.Label(root, text="My Daily Tasks", font=("Helvetica", 18, "bold"), bg="#f4f4f9", fg="#333")
title_label.pack(pady=15)

# Input Field for typing tasks
task_entry = tk.Entry(root, font=("Helvetica", 14), width=24, bd=2, relief="groove")
task_entry.pack(pady=10)

# Add Task Button
add_button = tk.Button(root, text="Add Task", bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"), bd=0, padx=10, pady=5, command=add_task)
add_button.pack(pady=5)

# Listbox to display the tasks
task_listbox = tk.Listbox(root, font=("Helvetica", 12), width=35, height=12, selectbackground="#a6a6a6", bd=2, relief="groove")
task_listbox.pack(pady=15)

# Frame to hold the bottom buttons side-by-side
button_frame = tk.Frame(root, bg="#f4f4f9")
button_frame.pack(pady=5)

# Delete Task Button
delete_button = tk.Button(button_frame, text="Delete Selected", bg="#f44336", fg="white", font=("Helvetica", 11, "bold"), bd=0, padx=10, pady=5, command=delete_task)
delete_button.grid(row=0, column=0, padx=10)

# Clear All Button
clear_button = tk.Button(button_frame, text="Clear All", bg="#ff9800", fg="white", font=("Helvetica", 11, "bold"), bd=0, padx=10, pady=5, command=clear_tasks)
clear_button.grid(row=0, column=1, padx=10)

# --- Start the Application ---
root.mainloop()