class BankAccount:

    # Class Variable
    ROI = 10.5

    # Constructor
    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    # Display Details
    def Display(self):
        print("\nAccount Holder :", self.Name)
        print("Current Balance :", self.Amount)

    # Deposit Amount
    def Deposit(self):
        deposit = float(input("Enter amount to deposit: "))
        self.Amount = self.Amount + deposit
        print("Amount deposited successfully.")

    # Withdraw Amount
    def Withdraw(self):
        withdraw = float(input("Enter amount to withdraw: "))

        if withdraw <= self.Amount:
            self.Amount = self.Amount - withdraw
            print("Withdrawal successful.")
        else:
            print("Insufficient Balance.")

    # Calculate Interest
    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        print("Interest =", interest)


# ---------------- Main Program ----------------

obj1 = BankAccount("Sagar", 50000)
obj2 = BankAccount("Rahul", 30000)

print("----- Account 1 -----")
obj1.Display()
obj1.Deposit()
obj1.Display()
obj1.Withdraw()
obj1.Display()
obj1.CalculateInterest()

print("\n----- Account 2 -----")
obj2.Display()
obj2.Deposit()
obj2.Display()
obj2.Withdraw()
obj2.Display()
obj2.CalculateInterest()