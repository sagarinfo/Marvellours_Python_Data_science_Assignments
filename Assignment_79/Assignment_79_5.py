import tkinter as tk
from tkinter import messagebox

# Predefined credentials
VALID_USERNAME = "admin"
VALID_PASSWORD = "1234"

def login():
    username = entry_user.get()
    password = entry_pass.get()
    if username == VALID_USERNAME and password == VALID_PASSWORD:
        messagebox.showinfo("Login", "Login Successful!")
        result_label.config(text="Welcome, " + username, fg="green")
    else:
        messagebox.showerror("Login", "Invalid username or password")
        result_label.config(text="Login Failed", fg="red")

root = tk.Tk()
root.title("Basic Login Form")
root.geometry("300x250")

tk.Label(root, text="Username:").pack(pady=(15, 0))
entry_user = tk.Entry(root)
entry_user.pack()

tk.Label(root, text="Password:").pack(pady=(10, 0))
entry_pass = tk.Entry(root, show="*")
entry_pass.pack()

tk.Button(root, text="Login", command=login).pack(pady=12)
result_label = tk.Label(root, text="", font=("Arial", 11, "bold"))
result_label.pack()

root.mainloop()