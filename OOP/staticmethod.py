class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    #Instance Method 1
    def deposit(self, amount):
        self.balance += amount
        return f"New balance: {self.balance}"
    
    @staticmethod
    def bank_policy():
        return "All accounts must maintain a minimum balance of $100."
    
# Creating an instance and calling instance methods
account1 = BankAccount("123456789", "John Doe", 1000)
print(account1.deposit(500))
print(BankAccount.bank_policy())
