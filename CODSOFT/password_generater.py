import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    """Generates a random password based on the provided length."""
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showwarning("Warning", "Password length must be greater than 0.")
            return
            
        # Define complexity: letters, numbers, and symbols
        characters = string.ascii_letters + string.digits + string.punctuation
        secure_password = ''.join(random.choice(characters) for _ in range(length))
        
        # Display the result in the readonly entry box
        result_var.set(secure_password)
        
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid numeric length.")

# --- Main Window Setup ---
root = tk.Tk()
root.title("Secure Password Generator")
root.geometry("400x300")
root.config(bg="#f9f9f9")

# --- UI Elements ---
title_label = tk.Label(root, text="Password Generator", font=("Arial", 18, "bold"), bg="#f9f9f9", fg="#333")
title_label.pack(pady=20)

# Input for Length
length_frame = tk.Frame(root, bg="#f9f9f9")
length_frame.pack(pady=10)

length_label = tk.Label(length_frame, text="Enter Password Length: ", font=("Arial", 12), bg="#f9f9f9")
length_label.grid(row=0, column=0)

length_entry = tk.Entry(length_frame, font=("Arial", 12), width=5, justify="center")
length_entry.grid(row=0, column=1)
length_entry.insert(0, "12") # Default length is 12

# Generate Button
generate_btn = tk.Button(root, text="Generate Password", font=("Arial", 12, "bold"), bg="#008CBA", fg="white", padx=10, pady=5, bd=0, command=generate_password)
generate_btn.pack(pady=15)

# Display Result
result_var = tk.StringVar()
result_entry = tk.Entry(root, textvariable=result_var, font=("Courier", 14), width=25, justify="center", state="readonly", bd=2, relief="groove")
result_entry.pack(pady=10)

root.mainloop()