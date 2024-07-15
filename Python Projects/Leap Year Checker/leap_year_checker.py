def is_leap_year(year):
    """
    Check if the given year is a leap year according to the Gregorian calendar rules.
    
    Args:
    - year (int): The year to check.
    
    Returns:
    - bool: True if the year is a leap year, False otherwise.
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def main():
    print("Welcome to the Leap Year Checker!")
    print("This tool checks if a given year is a leap year according to the Gregorian calendar rules.")
    print("Enter 'q' at any time to quit the program.")
    
    while True:
        try:
            user_input = input("Enter a year (integer) or 'q' to quit: ").strip().lower()
            if user_input == 'q':
                print("Exiting the program. Goodbye!")
                return
            
            year = int(user_input)
            if year < 0:
                raise ValueError("Year must be a positive integer.")
            
            if is_leap_year(year):
                print(f"{year} is a leap year.")
            else:
                print(f"{year} is not a leap year.")
            
        except ValueError as ve:
            print(f"Error: {ve}. Please enter a valid year.")

if __name__ == "__main__":
    main()