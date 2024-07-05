class Account:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited: ${amount}")
        return f"${amount} deposited successfully."

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds."
        self.balance -= amount
        self.transaction_history.append(f"Withdrawn: ${amount}")
        return f"${amount} withdrawn successfully."

    def check_balance(self):
        return f"Your current balance is: ${self.balance}"

    def change_pin(self, old_pin, new_pin):
        if self.pin != old_pin:
            return "Incorrect old PIN."
        self.pin = new_pin
        return "PIN changed successfully."

    def get_transaction_history(self):
        return self.transaction_history if self.transaction_history else "No transactions yet."

class ATM:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account_number, pin, initial_balance=0):
        if account_number in self.accounts:
            return "Account already exists."
        self.accounts[account_number] = Account(account_number, pin, initial_balance)
        return "Account created successfully."

    def access_account(self, account_number, pin):
        if account_number not in self.accounts:
            return None, "Account not found."
        account = self.accounts[account_number]
        if account.pin != pin:
            return None, "Incorrect PIN."
        return account, "Access granted."

def main():
    atm = ATM()
    print("Welcome to the ATM Machine Simulation")
    
    while True:
        print("\n1. Create Account")
        print("2. Access Account")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            account_number = input("Enter new account number: ")
            pin = input("Enter new PIN: ")
            initial_balance = float(input("Enter initial balance: "))
            print(atm.add_account(account_number, pin, initial_balance))

        elif choice == '2':
            account_number = input("Enter account number: ")
            pin = input("Enter PIN: ")
            account, message = atm.access_account(account_number, pin)
            print(message)
            if account:
                while True:
                    print("\n1. Check Balance")
                    print("2. Deposit Cash")
                    print("3. Withdraw Cash")
                    print("4. Change PIN")
                    print("5. Transaction History")
                    print("6. Logout")
                    sub_choice = input("Enter your choice: ")

                    if sub_choice == '1':
                        print(account.check_balance())
                    
                    elif sub_choice == '2':
                        amount = float(input("Enter amount to deposit: "))
                        print(account.deposit(amount))
                    
                    elif sub_choice == '3':
                        amount = float(input("Enter amount to withdraw: "))
                        print(account.withdraw(amount))
                    
                    elif sub_choice == '4':
                        old_pin = input("Enter old PIN: ")
                        new_pin = input("Enter new PIN: ")
                        print(account.change_pin(old_pin, new_pin))
                    
                    elif sub_choice == '5':
                        print(account.get_transaction_history())
                    
                    elif sub_choice == '6':
                        print("Logged out.")
                        break

                    else:
                        print("Invalid choice. Please try again.")

        elif choice == '3':
            print("Thank you for using the ATM Machine Simulation.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
