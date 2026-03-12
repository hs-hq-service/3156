class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            try:
                amount_str = input("Enter the amount to deposit: $")
                amount = float(amount_str)
                if amount < 0:
                    print("Amount must be positive.")
                else:
                    cb.deposit(amount)
            except ValueError:
                print("Error: Invalid input. Please enter a numeric value for the amount.")
        elif action.lower() == 'withdraw':
            try:
                amount_str = input("Enter the amount to withdraw: $")
                amount = float(amount_str)
                if amount < 0:
                    print("Amount must be positive.")
                else:
                    cb.withdraw(amount)
            except ValueError:
                print("Error: Invalid input. Please enter a numeric value for the amount.")
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
