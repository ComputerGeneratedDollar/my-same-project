import random
import os

BALANCE_FILE = "income_balance.txt"


def load_balance():
    if os.path.exists(BALANCE_FILE):
        with open(BALANCE_FILE, "r") as f:
            try:
                return float(f.read().strip())
            except ValueError:
                return 0.0
    return 0.0

def save_balance(balance):
    with open(BALANCE_FILE, "w") as f:
        f.write(f"{balance:.2f}")

def generate_income():
    # Simuliere Einkommen zwischen $10 und $100
    return round(random.uniform(10, 100), 2)

def print_ascii_dollar(amount):
    art = f"""
    _______________________
   |  _________________  |
   | | ComputerGenerated | |
   | |   Dollar Income   | |
   | |__________________| |
   |  ___ ___ ___   ___  |
   | | $ | $ | $ | | {amount:6.2f} |
   | |___|___|___| |_____| |
   |_______________________|
    """
    print(art)

def main():
    balance = load_balance()
    income = generate_income()
    balance += income
    save_balance(balance)
    print_ascii_dollar(income)
    print(f"You just earned: ${income:.2f}")
    print(f"Total ComputerGeneratedDollar: ${balance:.2f}")
    print("(Run this program again to generate more income!)")

if __name__ == "__main__":
    main()
