import tkinter as tk
from tkinter import messagebox
from tkinter import font

# Function to handle login button click
def login():
    username = username_entry.get()
    password = password_entry.get()

    # Check if username and password are correct
    # For demonstration, always accept "admin" / "password"
    if username == "admin" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create main window
root = tk.Tk()
root.title("Spoofer Login")

# Custom font for title
title_font = font.Font(family='Helvetica', size=20, weight='bold')

# Title Label
title_label = tk.Label(root, text="Bloxiis test!", font=title_font)
title_label.pack(pady=20)

# Username Label and Entry
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

# Password Label and Entry
password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Login Button with Animation
def on_enter(event):
    login_button["background"] = "#4CAF50"  # Green color

def on_leave(event):
    login_button["background"] = "#1E90FF"  # Default color

login_button = tk.Button(root, text="Login", width=10, height=2, bg="#1E90FF", fg="white", command=login)
login_button.pack(pady=20)
login_button.bind("<Enter>", on_enter)
login_button.bind("<Leave>", on_leave)

# Run the Tkinter event loop
root.mainloop()
