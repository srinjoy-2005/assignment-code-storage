import random

class BankAccount:
    account_numbers = set()
    
    def __init__(self):
        self.balance = 0
        x = random.randint(int(1e7),int(1e10))
        self.account_num = x
        while x in self.account_numbers:
            x = random.randint(int(1e7),int(1e10))
            self.account_num = x
        self.account_numbers.add(self.account_num)
        self.pin = None
    
    def deposit(self,amount):
        self.balance += amount
    
    def withdrdaw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient Balance")

    def get_balance(self):
        return self.balance
    
    def change_pin(self,new_pin):
        self.pin = new_pin

class SavingsAccount(BankAccount):
    def __init__(self):
        super().__init__()
        self.interest_rate = 10
    
    def pay_interest(self):
        self.balance += self.interest_rate * self.balance / 100

    def update_interest(self,ir):
        self.interest_rate = ir

class FeeSavingsAccount(SavingsAccount):
    def __init__(self):
        super().__init__()
        self.fee = 100

    def withdrdaw(self, amount):
        return super().withdrdaw(amount+self.fee)
    
    def update_fee(self,f):
        self.fee = f

def main():
    accounts = {}
    print("--- Bank Account Management System ---")
    
    while True:
        print("\nMain Menu:")
        print("1. Create New Account")
        print("2. Select Account (Transactions)")
        print("3. Exit")
        
        choice = input("Select an option: ")

        if choice == '1':
            new_acc = FeeSavingsAccount()
            print(f"Account Created! Number: {new_acc.account_num}")
            p = input("Set your 4-digit PIN: ")
            new_acc.change_pin(p)
            accounts[str(new_acc.account_num)] = new_acc

        elif choice == '2':
            acc_num = input("Enter Account Number: ")
            if acc_num in accounts:
                acc = accounts[acc_num]
                
                print("\n1. Balance 2. Deposit 3. Withdraw 4. Interest 5. Change PIN")
                sub_choice = input("Select: ")

                if sub_choice in ['2', '3']:
                    verify_pin = input("Enter PIN to authorize: ")
                    if verify_pin != acc.pin:
                        print("Incorrect PIN. Transaction denied.")
                        continue

                if sub_choice == '1':
                    print(f"Balance: {acc.get_balance()}")
                elif sub_choice == '2':
                    amt = float(input("Deposit Amount: "))
                    acc.deposit(amt)
                elif sub_choice == '3':
                    amt = float(input("Withdraw Amount: "))
                    acc.withdrdaw(amt)
                elif sub_choice == '4':
                    acc.pay_interest()
                    print("Interest added.")
                elif sub_choice == '5':
                    old_pin = input("Enter current PIN: ")
                    if old_pin == acc.pin:
                        acc.change_pin(input("Enter new PIN: "))
                    else:
                        print("Auth failed.")
            else:
                print("Account not found.")

        elif choice == '3':
            break

if __name__ == "__main__":
    main()