import tkinter as tk
from tkinter import messagebox

def find_max():
    try:
        nums = [float(e.get()) for e in (entry1, entry2, entry3)]
        result_label.config(text=f"Largest = {max(nums)}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

root = tk.Tk()
root.title("Find the Largest Number")
root.geometry("300x300")

entries = []
for i, text in enumerate(["First Number:", "Second Number:", "Third Number:"]):
    tk.Label(root, text=text).pack(pady=(10, 0))
    e = tk.Entry(root)
    e.pack()
    entries.append(e)
entry1, entry2, entry3 = entries

tk.Button(root, text="Find Maximum", command=find_max).pack(pady=12)
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack()

root.mainloop()