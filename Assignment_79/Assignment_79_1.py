import tkinter as tk
from tkinter import messagebox

def add():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        result_label.config(text=f"Sum = {a + b}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

root = tk.Tk()
root.title("Addition of Two Numbers")
root.geometry("300x220")

tk.Label(root, text="First Number:").pack(pady=(15, 0))
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Second Number:").pack(pady=(10, 0))
entry2 = tk.Entry(root)
entry2.pack()

tk.Button(root, text="Add", command=add).pack(pady=12)
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack()

root.mainloop()