import tkinter as tk

def button_click(item):
    """Handles button clicks and updates the display."""
    current = display_var.get()
    display_var.set(current + str(item))

def button_clear():
    """Clears the display."""
    display_var.set("")

def button_equal():
    """Evaluates the mathematical expression and shows the result."""
    try:
        # eval() computes the math expression passed as a string
        result = str(eval(display_var.get()))
        display_var.set(result)
    except ZeroDivisionError:
        display_var.set("Div by Zero Error")
    except Exception:
        display_var.set("Error")

# --- Main Window Setup ---
root = tk.Tk()
root.title("GUI Calculator")
root.geometry("320x420")
root.resizable(0, 0) # Prevents resizing of the window
root.config(bg="#2c3e50")

display_var = tk.StringVar()

# --- Display Screen ---
display_entry = tk.Entry(root, textvariable=display_var, font=("Helvetica", 20, "bold"), bg="#ecf0f1", fg="#2c3e50", bd=10, justify="right")
display_entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=20, pady=10)

# --- Button Layout ---
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Create and place buttons dynamically
for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, font=("Helvetica", 16, "bold"), bg="#27ae60", fg="white", width=5, height=2, command=button_equal)
    elif text == 'C':
        btn = tk.Button(root, text=text, font=("Helvetica", 16, "bold"), bg="#e74c3c", fg="white", width=5, height=2, command=button_clear)
    elif text in ['/', '*', '-', '+']:
        btn = tk.Button(root, text=text, font=("Helvetica", 16, "bold"), bg="#f39c12", fg="white", width=5, height=2, command=lambda t=text: button_click(t))
    else:
        btn = tk.Button(root, text=text, font=("Helvetica", 16, "bold"), bg="#34495e", fg="white", width=5, height=2, command=lambda t=text: button_click(t))
    
    btn.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()