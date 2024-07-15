class InterestCalculator:
    def __init__(self, principal, rate, time):
        self.principal = principal
        self.rate = rate / 100  # Convert percentage to decimal
        self.time = time

    def simple_interest(self):
        """Calculate simple interest."""
        return self.principal * self.rate * self.time

    def compound_interest(self, n):
        """
        Calculate compound interest.
        
        Parameters:
        n (int): Number of times interest applied per time period.
        """
        return self.principal * (1 + self.rate / n) ** (n * self.time) - self.principal

    def continuous_compound_interest(self):
        """Calculate continuous compound interest."""
        import math
        return self.principal * (math.exp(self.rate * self.time) - 1)

    def total_amount(self, interest_type='simple', n=1):
        """
        Calculate total amount after interest.
        
        Parameters:
        interest_type (str): Type of interest calculation ('simple', 'compound', 'continuous').
        n (int): Number of times interest applied per time period for compound interest.
        """
        if interest_type == 'simple':
            interest = self.simple_interest()
        elif interest_type == 'compound':
            interest = self.compound_interest(n)
        elif interest_type == 'continuous':
            interest = self.continuous_compound_interest()
        else:
            raise ValueError("Invalid interest type. Choose 'simple', 'compound', or 'continuous'.")
        
        return self.principal + interest

    def monthly_payment(self, interest_type='simple', n=1):
        """
        Calculate monthly payment.
        
        Parameters:
        interest_type (str): Type of interest calculation ('simple', 'compound', 'continuous').
        n (int): Number of times interest applied per time period for compound interest.
        """
        total_amount = self.total_amount(interest_type, n)
        months = self.time * 12
        return total_amount / months

    def display_results(self, interest_type='simple', n=1):
        """
        Display the results of the interest calculation.
        
        Parameters:
        interest_type (str): Type of interest calculation ('simple', 'compound', 'continuous').
        n (int): Number of times interest applied per time period for compound interest.
        """
        total_amount = self.total_amount(interest_type, n)
        monthly_payment = self.monthly_payment(interest_type, n)
        print(f"Principal: ${self.principal:.2f}")
        print(f"Rate: {self.rate * 100:.2f}%")
        print(f"Time: {self.time:.2f} years")
        if interest_type == 'simple':
            print(f"Simple Interest: ${self.simple_interest():.2f}")
        elif interest_type == 'compound':
            print(f"Compound Interest (compounded {n} times per year): ${self.compound_interest(n):.2f}")
        elif interest_type == 'continuous':
            print(f"Continuous Compound Interest: ${self.continuous_compound_interest():.2f}")
        print(f"Total Amount after {self.time:.2f} years: ${total_amount:.2f}")
        print(f"Monthly Payment: ${monthly_payment:.2f}")

def main():
    # Welcome
    print("Welcome to the Interest Payment Calculator!")
    print("This program will calculate interest and monthly payments based on your input.")

    # Get user input
    principal = float(input("Enter the principal amount in dollars: "))
    rate = float(input("Enter the annual interest rate (in %): "))
    time = float(input("Enter the time period in years: "))
    interest_type = input("Enter the interest type ('simple', 'compound', 'continuous'): ").strip().lower()
    n = 1  # Default value for compounding periods

    if interest_type == 'compound':
        n = int(input("Enter the number of times interest is compounded per year: "))

    # Create calculator instance and display results
    calculator = InterestCalculator(principal, rate, time)
    calculator.display_results(interest_type, n)

if __name__ == "__main__":
    main()