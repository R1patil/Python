class BankAccount:
    def __init__(self,account_number,account_holder,account_balance=0.0):
        self.account_number=account_number
        self.account_holder=account_holder
        self.initial_amount=account_balance

    def deposit(self,amount):
        if amount>0:
            self.initial_amount+=amount
            print(f"Deposited: {amount}. New balance: {self.initial_amount}")
        else: 
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount): 
        if amount <= 0: 
            print("Withdrawal amount must be positive.") 
        elif amount > self.initial_amount: 
            print("Insufficient funds.") 
        else: 
            self.initial_amount -= amount 
            print(f"Withdrawn: {amount}. New balance: {self.initial_amount}") 
            
        # Method to display balance 
        
    def display_balance(self): 
        print(f"Account Holder: {self.account_holder}") 
        print(f"Account Number: {self.account_number}") 
        print(f"Current Balance: {self.initial_amount}")
    
# Create account objects
account1 = BankAccount("12345", "Alice", 500)
account2 = BankAccount("67890", "Bob", 1000)

# Perform operations
account1.deposit(200)
account1.withdraw(100)
account1.display_balance()

account2.withdraw(1200)  # Should show insufficient funds
account2.display_balance()
