import random
import string

def generate_random_password(length=12, include_symbols=True):
    """
    Generate a random password.

    Parameters:
    length (int): Length of the password (default is 12).
    include_symbols (bool): Whether to include symbols in the password (default is True).

    Returns:
    str: Generated random password.
    """
    # Define character sets
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation if include_symbols else ''

    # Combine character sets based on include_symbols flag
    characters = letters + digits + symbols

    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

def main():
    # Welcome
    print("Welcome to the Random Password Generator!")
    print("This program will generate a random password based on your specifications.")

    try:
        length = int(input("Enter the length of the password: "))
        include_symbols = input("Include symbols in the password? (y/n): ").strip().lower() == 'y'
    except ValueError:
        print("Invalid input. Using default values.")
        length = 12
        include_symbols = True

    password = generate_random_password(length, include_symbols)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()