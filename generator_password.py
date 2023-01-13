import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():
    length = int(entry.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for i in range(length))
    messagebox.showinfo("Generated password", password)

root = tk.Tk()
root.title("Password Generator")

label = tk.Label(root, text="Enter the desired length of the password:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Generate", command=generate_password)
button.pack()

root.mainloop()
