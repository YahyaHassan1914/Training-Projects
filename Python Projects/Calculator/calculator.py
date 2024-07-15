import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def power(x, y):
    return x ** y

def sqrt(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return "Error! Square root of a negative number."

def log(x, base=10):
    if x > 0:
        return math.log(x, base)
    else:
        return "Error! Logarithm of non-positive number."

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

def factorial(x):
    if x >= 0:
        return math.factorial(x)
    else:
        return "Error! Factorial of a negative number."

def menu():
    print("Advanced Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. Logarithm")
    print("8. Sine")
    print("9. Cosine")
    print("10. Tangent")
    print("11. Factorial")
    print("12. Exit")

def main():
    while True:
        menu()
        choice = input("Select operation (1-12): ")
        
        if choice == '12':
            print("Exiting the calculator.")
            break
        
        if choice in ['1', '2', '3', '4', '5']:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
        
        if choice == '1':
            print("Result:", add(x, y))
        elif choice == '2':
            print("Result:", subtract(x, y))
        elif choice == '3':
            print("Result:", multiply(x, y))
        elif choice == '4':
            print("Result:", divide(x, y))
        elif choice == '5':
            print("Result:", power(x, y))
        elif choice == '6':
            x = float(input("Enter number: "))
            print("Result:", sqrt(x))
        elif choice == '7':
            x = float(input("Enter number: "))
            base = input("Enter base (default is 10): ")
            base = float(base) if base else 10
            print("Result:", log(x, base))
        elif choice == '8':
            x = float(input("Enter angle in degrees: "))
            print("Result:", sin(x))
        elif choice == '9':
            x = float(input("Enter angle in degrees: "))
            print("Result:", cos(x))
        elif choice == '10':
            x = float(input("Enter angle in degrees: "))
            print("Result:", tan(x))
        elif choice == '11':
            x = int(input("Enter number: "))
            print("Result:", factorial(x))
        else:
            print("Invalid input. Please enter a number between 1 and 12.")
        
        input("Press Enter to continue...\n\n")

if __name__ == "__main__":
    main()
