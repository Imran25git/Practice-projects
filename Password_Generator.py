import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Ask user for desired password length
try:
    length = int(input("Enter the desired password length: "))
    if length <= 5:
        print("For security, choose a length of 6 or more.")
    else:
        print("Generated password:", generate_password(length))
except ValueError:
    print("Please enter a valid number.")
