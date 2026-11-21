class BankAccount:
    def __init__(self, ac_no, name, ac_type, balance):
        self.ac_no = ac_no
        self.name = name
        self.ac_type = ac_type
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited successfully!")
        print("Current balance:", self.balance)

    def withdrawal(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn successfully!")
            print("Current balance:", self.balance)
        else:
            print("Insufficient balance!")

    def display(self):
        print("\nAccount Details")
        print("Account Number:", self.ac_no)
        print("Name:", self.name)
        print("Account Type:", self.ac_type)
        print("Balance:", self.balance)


# Creating an object
ac = BankAccount(101, "Arun", "Savings", 5000)

# Display account details
ac.display()

# Deposit amount
ac.deposit(2000)

# Withdraw amount
ac.withdrawal(1000)
