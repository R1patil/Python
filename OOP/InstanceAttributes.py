class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number # instance attribute
        self.account_holder = account_holder # instance attribute
        self.balance = balance # instance attribute
# Creating an instance of BankAccount
account1 = BankAccount("123456789", "John Doe", 1000)
print(account1.account_number) # Output: 123456789
print(account1.account_holder) # Output: John Doe
print(account1.balance) # Output: 1000