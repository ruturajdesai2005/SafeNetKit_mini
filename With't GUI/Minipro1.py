import random
import time
import itertools
import string

# Secure Password Generator: Random letters + Special + Mobile + Birthdate1
def generate_password():
    special_symbols = "!@#$%^&*()"

    name = input("Enter your name: ")
    birthdate = input("Enter your birthdate (DDMMYYYY): ")
    mobile = input("Enter your mobile number: ")

    if len(name) < 4 or len(mobile) < 2 or len(birthdate) < 2:
        print("Please ensure name has at least 4 letters, and mobile/birthdate have at least 2 digits.")
        return

    name_letters = ''.join(random.sample(name, 4))
    mobile_digits = ''.join(random.sample(mobile, 2))
    birth_digits = ''.join(random.sample(birthdate, 2))
    special_char = random.choice(special_symbols)

    password = name_letters + special_char + mobile_digits + birth_digits
    print(f"Generated Password: {password}")

# Brute Force Attack Simulator
def brute_force_attack(target_password):
    chars = string.ascii_letters + string.digits + string.punctuation
    attempts = 0
    start_time = time.time()

    for length in range(1, len(target_password) + 1):
        for guess in itertools.product(chars, repeat=length):
            attempts += 1
            guess = "".join(guess)
            if guess == target_password:
                end_time = time.time()
                print(f"🔓 Password found: {guess} in {attempts} attempts and {end_time - start_time:.2f} seconds")
                return

    print("Brute force failed (Password too complex)")

# Simple Login System with Hashing
def simple_hash(password):
    return ''.join(chr(ord(char) + 3) for char in password)

def register():
    username = input("Enter username: ")
    password = input("Enter password: ")
    hashed_password = simple_hash(password)

    with open("users.txt", "a") as file:
        file.write(f"{username},{hashed_password}\n")

    print("User registered successfully!")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    hashed_password = simple_hash(password)

    try:
        with open("users.txt", "r") as file:
            users = file.readlines()

        for user in users:
            stored_user, stored_password = user.strip().split(",")
            if username == stored_user and hashed_password == stored_password:
                print("Login successful!")
                return
        print("Invalid username or password.")
    except FileNotFoundError:
        print("No users found. Please register first.")

# Phishing URL Detector
def check_phishing(url):
    if "@" in url:
        print("Warning: URL contains '@', which is a phishing indicator.")
    if url.count('-') > 2:
        print("Warning: Too many hyphens, possible phishing attempt.")
    if url.replace('.', '').isdigit():
        print("Warning: URL contains an IP address instead of a domain.")
    else:
        print("URL seems safe.")

# CAPTCHA Generator
def generate_captcha():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))

def verify_captcha():
    captcha = generate_captcha()
    print(f"CAPTCHA: {captcha}")
    user_input = input("Enter the CAPTCHA: ")

    if user_input == captcha:
        print("CAPTCHA verification successful!")
    else:
        print("CAPTCHA incorrect. Try again.")

# ----------- Menu System -----------
while True:
    print("\n===== Cybersecurity Mini Projects =====")
    print("1. Secure Password Generator")
    print("2. Brute Force Attack Simulator")
    print("3. Simple Login System with Hashing")
    print("4. Phishing URL Detector")
    print("5. CAPTCHA Generator")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        generate_password()
    elif choice == "2":
        password = input("Enter a password to test brute-force attack: ")
        brute_force_attack(password)
    elif choice == "3":
        sub_choice = input("Register or Login (r/l): ").lower()
        if sub_choice == "r":
            register()
        elif sub_choice == "l":
            login()
        else:
            print("Invalid option.")
    elif choice == "4":
        url = input("Enter a URL to check: ")
        check_phishing(url)
    elif choice == "5":
        verify_captcha()
    elif choice == "6":
        print("Exiting... Thank you!")
        break
    else:
        print("Invalid choice, please try again.")