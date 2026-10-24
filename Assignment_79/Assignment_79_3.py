import math
import tkinter as tk
from tkinter import messagebox

def calculate_area():
    try:
        r = float(entry_radius.get())
        if r < 0:
            messagebox.showerror("Error", "Radius cannot be negative")
            return
        area = math.pi * r ** 2
        result_label.config(text=f"Area = {area:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

root = tk.Tk()
root.title("Area of Circle")
root.geometry("300x200")

tk.Label(root, text="Radius:").pack(pady=(15, 0))
entry_radius = tk.Entry(root)
entry_radius.pack()

tk.Button(root, text="Calculate Area", command=calculate_area).pack(pady=12)
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack()

root.mainloop()