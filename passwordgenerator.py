import random
import string

def generate_password(length):
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets
    all_characters = lowercase + uppercase + digits + special_characters

    # Ensure the password is complex by including at least one character from each set
    if length < 4:
        print("Password length should be at least 4 characters to include all character types.")
        return None

    # Generate a password
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_characters)
    ]

    # Fill the rest of the password length with random characters
    password += [random.choice(all_characters) for _ in range(length - 4)]

    # Shuffle the password to ensure randomness
    random.shuffle(password)

    return ''.join(password)

def main():
    print("Welcome to the Password Generator!")

    # Get user input for password length
    try:
        length = int(input("Enter the desired length of the password: "))
        if length < 1:
            print("Password length must be at least 1.")
            return
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return

    # Generate and display the password
    password = generate_password(length)
    if password:
        print(f"Generated Password: {password}")

# Run the main function
main()
