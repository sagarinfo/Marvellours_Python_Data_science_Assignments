class Numbers:

    # Constructor
    def __init__(self, Value):
        self.Value = Value

    # Check Prime
    def ChkPrime(self):
        if self.Value <= 1:
            return False

        for i in range(2, self.Value):
            if self.Value % i == 0:
                return False

        return True

    # Check Perfect Number
    def ChkPerfect(self):
        sum = 0

        for i in range(1, self.Value):
            if self.Value % i == 0:
                sum = sum + i

        if sum == self.Value:
            return True
        else:
            return False

    # Display Factors
    def Factors(self):
        print("Factors are:")
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i, end=" ")
        print()

    # Sum of Factors
    def SumFactors(self):
        sum = 0

        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                sum = sum + i

        return sum


# ---------------- Main Program ----------------

num1 = int(input("Enter first number: "))
obj1 = Numbers(num1)

print("\nFirst Number:", num1)

if obj1.ChkPrime():
    print("Prime Number")
else:
    print("Not a Prime Number")

if obj1.ChkPerfect():
    print("Perfect Number")
else:
    print("Not a Perfect Number")

obj1.Factors()
print("Sum of Factors:", obj1.SumFactors())


num2 = int(input("\nEnter second number: "))
obj2 = Numbers(num2)

print("\nSecond Number:", num2)

if obj2.ChkPrime():
    print("Prime Number")
else:
    print("Not a Prime Number")

if obj2.ChkPerfect():
    print("Perfect Number")
else:
    print("Not a Perfect Number")

obj2.Factors()
print("Sum of Factors:", obj2.SumFactors())