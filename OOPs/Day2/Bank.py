class bank:
    # class var
    bankname = "SBI"
    ifsc = "SBI0001"

    #instance var
    def __init__(self,name,balance,mail):
        self.name = name
        self.balance = balance
        self.mail = mail

    # Method ins
    def show_details(self):
        print(f"Name: {self.name}\nBalance: {self.balance}\nMail: {self.mail}\nBank Name: {self.bankname}\nIFSC: {self.ifsc}")

    def check_balance(self):
        print("Available balance is:",self.balance)

    def deposit(self):
        dep_amt = int(input("Put the amount you want to deposit:"))
        self.balance += dep_amt
        print("Current Balance:",self.balance)


    def withdraw(self):
        with_amt = int(input("Put the amount you want to withdraw:"))
        self.balance -= with_amt
        print("Withdraw Successful")
        print("Current Balance:",self.balance)

    def intrest(self):
        int_amt = int(input("Enter the amount you want to deposit to check intrest:"))
        a = print("1.3 months with a intrest of 7%\n2.6 Months with a intrest of 10%\n3.12 Months with a intrest of 12%")
        ch = int(input("Enter your choice: "))
        match ch:
            case 1:
                intrest = int_amt*(1.00+0.07)**0.3
                total = intrest - int_amt
                print(f"Your intrest will be: {total}")

            case 2:
                intrest = int_amt*(1.00+0.10)**0.6
                total = intrest - int_amt
                print(f"Your intrest will be: {total}")

            case 3:
                intrest = int_amt*(1.00+0.12)**0.12
                total = intrest - int_amt
                print(f"Your intrest will be: {total}")

    def compare(self):
        if user1.balance > user2.balance:
            print("User 1 has more money!")
        else:
            print("User 2 has more money")



user1 = bank("Ram", 0, "ram123@gmail.com")
user2 = bank("Shyam", 0, "shyam123@gmail.com")
user1.show_details()
user1.check_balance()
user1.deposit()
user2.deposit()
user1.check_balance()
user1.withdraw()
user1.check_balance()
user1.intrest()
user1.compare()