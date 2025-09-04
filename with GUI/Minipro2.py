import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import random
import time
import itertools
import string
import os

# ---------- Function Definitions ----------

def generate_password_gui():
    def generate():
        name = name_entry.get()
        birthdate = birth_entry.get()
        mobile = mobile_entry.get()
        special_symbols = "!@#$%^&*()"

        if len(name) < 4 or len(mobile) < 2 or len(birthdate) < 2:
            messagebox.showerror("Error", "Ensure name has 4+ letters, and mobile/birthdate have 2+ digits.")
            return

        name_letters = ''.join(random.sample(name, 4))
        mobile_digits = ''.join(random.sample(mobile, 2))
        birth_digits = ''.join(random.sample(birthdate, 2))
        special_char = random.choice(special_symbols)

        password = name_letters + special_char + mobile_digits + birth_digits
        result_label.config(text=f"Generated Password: {password}")

    win = tk.Toplevel(root)
    win.title("Password Generator")

    tk.Label(win, text="Name:").pack()
    name_entry = tk.Entry(win)
    name_entry.pack()

    tk.Label(win, text="Birthdate (DDMMYYYY):").pack()
    birth_entry = tk.Entry(win)
    birth_entry.pack()

    tk.Label(win, text="Mobile Number:").pack()
    mobile_entry = tk.Entry(win)
    mobile_entry.pack()

    tk.Button(win, text="Generate Password", command=generate).pack(pady=5)
    result_label = tk.Label(win, text="")
    result_label.pack()

def brute_force_gui():
    def simulate():
        password = password_entry.get()
        if not password:
            messagebox.showerror("Error", "Enter a password to test.")
            return

        chars = string.ascii_letters + string.digits + string.punctuation
        attempts = 0
        start_time = time.time()

        for length in range(1, len(password) + 1):
            for guess in itertools.product(chars, repeat=length):
                attempts += 1
                guess = ''.join(guess)
                if guess == password:
                    elapsed = time.time() - start_time
                    messagebox.showinfo("Brute Force", f"🔓 Found: {guess}\nAttempts: {attempts}\nTime: {elapsed:.2f}s")
                    return

        messagebox.showinfo("Brute Force", "Password not found.")

    win = tk.Toplevel(root)
    win.title("Brute Force Simulator")

    tk.Label(win, text="Enter Password to Crack:").pack()
    password_entry = tk.Entry(win, show="*")
    password_entry.pack()

    tk.Button(win, text="Start Brute Force", command=simulate).pack(pady=5)

def simple_hash(password):
    return ''.join(chr(ord(c) + 3) for c in password)

def register_user():
    username = simpledialog.askstring("Register", "Enter username:")
    password = simpledialog.askstring("Register", "Enter password:", show="*")
    if username and password:
        hashed = simple_hash(password)
        with open("users.txt", "a") as f:
            f.write(f"{username},{hashed}\n")
        messagebox.showinfo("Register", "User registered!")

def login_user():
    username = simpledialog.askstring("Login", "Enter username:")
    password = simpledialog.askstring("Login", "Enter password:", show="*")
    if username and password:
        hashed = simple_hash(password)
        try:
            with open("users.txt", "r") as f:
                users = f.readlines()
            for u in users:
                stored_user, stored_pass = u.strip().split(",")
                if username == stored_user and hashed == stored_pass:
                    messagebox.showinfo("Login", "Login successful!")
                    return
            messagebox.showerror("Login", "Invalid credentials.")
        except FileNotFoundError:
            messagebox.showerror("Error", "No users found. Register first.")

def login_system_gui():
    win = tk.Toplevel(root)
    win.title("Login System")
    tk.Button(win, text="Register", command=register_user).pack(pady=5)
    tk.Button(win, text="Login", command=login_user).pack(pady=5)

def phishing_gui():
    def check():
        url = url_entry.get()
        if not url:
            return
        alerts = []
        if "@" in url:
            alerts.append("Contains '@' symbol – suspicious.")
        if url.count('-') > 2:
            alerts.append("Too many hyphens – could be phishing.")
        if url.replace('.', '').isdigit():
            alerts.append("Uses IP address – risky.")
        if alerts:
            messagebox.showwarning("Phishing Warning", "\n".join(alerts))
        else:
            messagebox.showinfo("Safe", "URL seems safe.")

    win = tk.Toplevel(root)
    win.title("Phishing URL Detector")
    tk.Label(win, text="Enter URL:").pack()
    url_entry = tk.Entry(win, width=40)
    url_entry.pack()
    tk.Button(win, text="Check URL", command=check).pack(pady=5)

def captcha_gui():
    def generate():
        nonlocal captcha_code
        captcha_code = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        captcha_label.config(text=captcha_code)

    def verify():
        if input_entry.get() == captcha_code:
            messagebox.showinfo("CAPTCHA", "Verification successful!")
        else:
            messagebox.showerror("CAPTCHA", "Incorrect CAPTCHA.")

    captcha_code = ""
    win = tk.Toplevel(root)
    win.title("CAPTCHA Verification")

    captcha_label = tk.Label(win, text="", font=("Helvetica", 18))
    captcha_label.pack(pady=5)
    generate()

    input_entry = tk.Entry(win)
    input_entry.pack()

    tk.Button(win, text="Verify", command=verify).pack(pady=5)
    tk.Button(win, text="Refresh CAPTCHA", command=generate).pack(pady=5)

# ---------- Main Window ----------

root = tk.Tk()
root.title("SafeNetKit - Cybersecurity Toolkit")
root.geometry("350x400")

tk.Label(root, text="SafeNetKit", font=("Helvetica", 18, "bold")).pack(pady=10)
tk.Button(root, text="1. Password Generator", width=30, command=generate_password_gui).pack(pady=5)
tk.Button(root, text="2. Brute Force Simulator", width=30, command=brute_force_gui).pack(pady=5)
tk.Button(root, text="3. Login System", width=30, command=login_system_gui).pack(pady=5)
tk.Button(root, text="4. Phishing URL Detector", width=30, command=phishing_gui).pack(pady=5)
tk.Button(root, text="5. CAPTCHA Generator", width=30, command=captcha_gui).pack(pady=5)
tk.Button(root, text="Exit", width=30, command=root.quit).pack(pady=10)

root.mainloop()