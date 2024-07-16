import requests
from prettytable import PrettyTable
import json

# Open the JSON file with api key
with open('api_key.json', 'r') as file:
    api_key = json.load(file)

API_KEY = api_key["api_key"]  # Replace with your ExchangeRate-API key
BASE_URL = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/'

class QuitProgramException(Exception):
    pass

def fetch_rates(base_currency):
    try:
        response = requests.get(BASE_URL + base_currency)
        data = response.json()
        if data['result'] == 'success':
            return data['conversion_rates']
        else:
            print("Error fetching rates:", data['error-type'])
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def convert_currency(amount, from_currency, to_currency, rates, precision):
    if from_currency != 'USD':
        amount = amount / rates[from_currency]
    return round(amount * rates[to_currency], precision)

def display_rates(rates):
    table = PrettyTable()
    table.field_names = ["Currency", "Rate"]
    for currency, rate in rates.items():
        table.add_row([currency, rate])
    print(table)

def get_input(prompt):
    user_input = input(prompt).strip().upper()
    if user_input == 'Q':
        raise QuitProgramException
    return user_input

def quit_program():
    print("Quitting the program. Goodbye!")
    exit()

def main():
    print("Welcome to the Advanced Currency Converter!")
    print("This tool allows you to convert amounts between different currencies using real-time exchange rates.")
    print("You can press 'q' at any prompt to quit the program.")

    try:
        while True:
            base_currency = get_input("Enter base currency (default is USD): ")
            if not base_currency:
                base_currency = 'USD'

            rates = fetch_rates(base_currency)
            
            if rates:
                display_rates(rates)
                
                precision_input = get_input("Enter the number of decimal places for the output (default is 2): ")
                if precision_input.isdigit():
                    precision = int(precision_input)
                else:
                    precision = 2

                while True:
                    try:
                        amount_input = get_input("Enter amount: ")
                        amount = float(amount_input)
                    except ValueError:
                        print("Invalid amount. Please enter a numeric value.")
                        continue

                    from_currency = get_input("Enter currency to convert from: ")
                    to_currency = get_input("Enter currency to convert to: ")
                    
                    if from_currency in rates and to_currency in rates:
                        converted_amount = convert_currency(amount, from_currency, to_currency, rates, precision)
                        print(f"{amount} {from_currency} is {converted_amount:.{precision}f} {to_currency}")
                    else:
                        print("Invalid currency code. Please try again.")

                    again = get_input("Do you want to convert another amount? (yes/no): ").lower()
                    if again != 'yes':
                        raise QuitProgramException

    except QuitProgramException:
        quit_program()

if __name__ == "__main__":
    main()