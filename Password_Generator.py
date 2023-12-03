import tkinter as tk
from tkinter import ttk
import secrets
import string

class PasswordGenerator:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")

        self.length_label = ttk.Label(master, text="Password Length:")
        self.length_label.grid(row=0, column=0, padx=10, pady=10)

        self.length_var = tk.StringVar()
        self.length_entry = ttk.Entry(master, textvariable=self.length_var)
        self.length_entry.grid(row=0, column=1, padx=10, pady=10)

        self.strength_label = ttk.Label(master, text="Password Strength:")
        self.strength_label.grid(row=1, column=0, padx=10, pady=10)

        self.strength_var = tk.StringVar()
        self.strength_var.set("Basic")

        self.basic_radio = ttk.Radiobutton(master, text="Basic", variable=self.strength_var, value="Basic")
        self.basic_radio.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        self.medium_radio = ttk.Radiobutton(master, text="Medium", variable=self.strength_var, value="Medium")
        self.medium_radio.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        self.advanced_radio = ttk.Radiobutton(master, text="Advanced", variable=self.strength_var, value="Advanced")
        self.advanced_radio.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        self.generate_button = ttk.Button(master, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.result_var = tk.StringVar()
        self.result_label = ttk.Label(master, textvariable=self.result_var)
        self.result_label.grid(row=5, column=0, columnspan=2, pady=10)

    def generate_password(self):
        try:
            length = int(self.length_var.get())
            if length <= 0:
                raise ValueError("Length must be greater than zero.")

            strength = self.strength_var.get().lower()
            characters = ""
            
            if strength == "basic":
                characters = string.ascii_letters + string.digits
            elif strength == "medium":
                characters = string.ascii_letters + string.digits + string.punctuation
            elif strength == "advanced":
                characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_lowercase + string.ascii_uppercase
            password = ''.join(secrets.choice(characters) for _ in range(length))

            self.result_var.set("Generated Password: " + password)
        except ValueError as e:
            self.result_var.set(str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()


