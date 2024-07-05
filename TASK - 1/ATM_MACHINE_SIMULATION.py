class Account:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number  # Unique identifier for the account
        self.pin = pin  # Personal Identification Number for authentication
        self.balance = balance  # Initial balance of the account
        self.transaction_history = []  # List to store the transaction history

    def deposit(self, amount):
        self.balance += amount  # Add the deposit amount to the balance
        self.transaction_history.append(f"Deposited: ${amount}")  # Record the deposit transaction
        return f"${amount} deposited successfully."

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds."  # Check if there are enough funds to withdraw
        self.balance -= amount  # Subtract the withdrawal amount from the balance
        self.transaction_history.append(f"Withdrawn: ${amount}")  # Record the withdrawal transaction
        return f"${amount} withdrawn successfully."

    def check_balance(self):
        return f"Your current balance is: ${self.balance}"  # Return the current balance

    def change_pin(self, old_pin, new_pin):
        if self.pin != old_pin:
            return "Incorrect old PIN."  # Check if the old PIN is correct
        self.pin = new_pin  # Update the PIN
        return "PIN changed successfully."

    def get_transaction_history(self):
        return self.transaction_history if self.transaction_history else "No transactions yet."  # Return the transaction history or a message if no transactions

class ATM:
    def __init__(self):
        self.accounts = {}  # Dictionary to store all accounts

    def add_account(self, account_number, pin, initial_balance=0):
        if account_number in self.accounts:
            return "Account already exists."  # Check if the account already exists
        self.accounts[account_number] = Account(account_number, pin, initial_balance)  # Create a new account
        return "Account created successfully."

    def access_account(self, account_number, pin):
        if account_number not in self.accounts:
            return None, "Account not found."  # Check if the account exists
        account = self.accounts[account_number]
        if account.pin != pin:
            return None, "Incorrect PIN."  # Check if the PIN is correct
        return account, "Access granted."

def main():
    atm = ATM()  # Create an ATM instance
    print("Welcome to the ATM Machine Simulation")
    
    while True:
        # Main menu
        print("\n1. Create Account")
        print("2. Access Account")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            # Create a new account
            account_number = input("Enter new account number: ")
            pin = input("Enter new PIN: ")
            initial_balance = float(input("Enter initial balance: "))
            print(atm.add_account(account_number, pin, initial_balance))

        elif choice == '2':
            # Access an existing account
            account_number = input("Enter account number: ")
            pin = input("Enter PIN: ")
            account, message = atm.access_account(account_number, pin)
            print(message)
            if account:
                while True:
                    # Account menu
                    print("\n1. Check Balance")
                    print("2. Deposit Cash")
                    print("3. Withdraw Cash")
                    print("4. Change PIN")
                    print("5. Transaction History")
                    print("6. Logout")
                    sub_choice = input("Enter your choice: ")

                    if sub_choice == '1':
                        # Check balance
                        print(account.check_balance())
                    
                    elif sub_choice == '2':
                        # Deposit cash
                        amount = float(input("Enter amount to deposit: "))
                        print(account.deposit(amount))
                    
                    elif sub_choice == '3':
                        # Withdraw cash
                        amount = float(input("Enter amount to withdraw: "))
                        print(account.withdraw(amount))
                    
                    elif sub_choice == '4':
                        # Change PIN
                        old_pin = input("Enter old PIN: ")
                        new_pin = input("Enter new PIN: ")
                        print(account.change_pin(old_pin, new_pin))
                    
                    elif sub_choice == '5':
                        # View transaction history
                        print(account.get_transaction_history())
                    
                    elif sub_choice == '6':
                        # Logout
                        print("Logged out.")
                        break

                    else:
                        print("Invalid choice. Please try again.")

        elif choice == '3':
            # Exit the program
            print("Thank you for using the ATM Machine Simulation.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()  # Run the main function
