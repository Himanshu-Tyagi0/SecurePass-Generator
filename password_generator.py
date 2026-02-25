import random
import string
import pyperclip

def weak_password(length):
    chars = string.ascii_lowercase
    return ''.join(random.choice(chars) for _ in range(length))

def medium_password(length):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def strong_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))


# ===== MENU =====
print("PASSWORD GENERATOR")
print("1. Weak Password")
print("2. Medium Password")
print("3. Strong Password")

choice = input("Enter your choice (1-3): ")

# custom length
try:
    length = int(input("Enter password length: "))
    if length <= 0:
        print("Length must be positive!")
        exit()
except ValueError:
    print("Please enter a valid number!")
    exit()

# generate password
if choice == "1":
    password = weak_password(length)

elif choice == "2":
    password = medium_password(length)

elif choice == "3":
    password = strong_password(length)

else:
    print("Invalid choice!")
    exit()

# copy to clipboard
pyperclip.copy(password)

print("\nGenerated Password:", password)

print("Password copied to clipboard!")
