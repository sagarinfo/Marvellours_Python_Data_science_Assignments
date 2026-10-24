import tkinter as tk
from tkinter import messagebox

def check_eligibility():
    name = entry_name.get().strip()
    if not name:
        messagebox.showerror("Error", "Please enter the name")
        return
    try:
        age = int(entry_age.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid age")
        return

    if age >= 18:
        result_label.config(text=f"{name} is eligible to vote", fg="green")
    else:
        result_label.config(text=f"{name} is not eligible to vote", fg="red")

root = tk.Tk()
root.title("Voting Eligibility Checker")
root.geometry("320x250")

tk.Label(root, text="Name:").pack(pady=(15, 0))
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Age:").pack(pady=(10, 0))
entry_age = tk.Entry(root)
entry_age.pack()

tk.Button(root, text="Check Eligibility", command=check_eligibility).pack(pady=12)
result_label = tk.Label(root, text="", font=("Arial", 11, "bold"))
result_label.pack()

root.mainloop()