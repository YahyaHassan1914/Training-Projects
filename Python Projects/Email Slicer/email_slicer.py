def email_slicer(email):
    try:
        username, domain = email.split('@')
        domain_name, tld = domain.split('.')
        return f"Username: {username}\nDomain Name: {domain_name}\nTop-Level Domain: {tld}"
    except ValueError:
        return "Invalid email format. Please enter a valid email address."

def main():
    print("Welcome to the Advanced Email Slicer!")
    email = input("Enter your email address: ").strip()
    result = email_slicer(email)
    print("\n" + result)

if __name__ == "__main__":
    main()