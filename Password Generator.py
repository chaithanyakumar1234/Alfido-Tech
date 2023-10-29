import random
import string

# Function to generate a secure password based on user-defined criteria
def generate_password(length, use_special_chars=False, use_numbers=False):
    characters = string.ascii_letters
    if use_special_chars:
        characters += string.punctuation
    if use_numbers:
        characters += string.digits

    if not characters:
        return "Invalid criteria for password generation."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Main program
if __name__ == "__main__":
    print("Password Generator - Secure Passwords for Online Accounts")

    # Prompt user for password length and criteria
    password_length = int(input("Enter the password length: "))
    include_special_chars = input("Include special characters? (yes/no): ").strip().lower() == "yes"
    include_numbers = input("Include numbers? (yes/no): ").strip().lower() == "yes"

    # Generate and display the password
    password = generate_password(password_length, include_special_chars, include_numbers)
    
    if password == "Invalid criteria for password generation.":
        print("Invalid criteria. Please include at least letters.")
    else:
        print("Generated Password:", password)
