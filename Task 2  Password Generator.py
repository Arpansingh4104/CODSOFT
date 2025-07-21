import random
import string
import tkinter as tk
from tkinter import simpledialog, messagebox

def generate_password(length, include_upper, include_digits, include_special):
    characters = list(string.ascii_lowercase)

    if include_upper:
        characters += list(string.ascii_uppercase)
    if include_digits:
        characters += list(string.digits)
    if include_special:
        characters += list("!@#$%^&*()-_=+[]{};:,.<>?/")

    if not characters:
        return "Error: No character set selected."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def prompt_user_and_generate():
    try:
        length = simpledialog.askinteger("Password Length", "Enter password length (min 4, max 32):", minvalue=4, maxvalue=32)
        if length is None:
            return

        use_upper = messagebox.askyesno("Include Uppercase?", "Include UPPERCASE letters?")
        use_digits = messagebox.askyesno("Include Digits?", "Include numbers?")
        use_special = messagebox.askyesno("Include Special Characters?", "Include symbols? (!, @, #, etc.)")

        password = generate_password(length, use_upper, use_digits, use_special)
        messagebox.showinfo("Generated Password", f"Your new password:\n\n{password}")

    except Exception as e:
        messagebox.showerror("Error", str(e))

def main():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    prompt_user_and_generate()

if __name__ == "__main__":
    main()
