class Airthmatic:
    
    
    def __init__(self,):
        self.Value1 = 0.0    # Instance variable
        self.Value2 = 0.0
        
    def Accept(self):
        self.Value1 = int(input("Enter first Number: "))
        self.Value2 = int(input("Enter second Number: "))
        
    def Addition(self):
        return self.Value1 + self.Value2
    
    def Substraction(self):
        return self.Value1 - self.Value2
    
    def Multiplication(self):
        return self.Value1 * self.Value2
    
    def Division(self):
        return self.Value1 / self.Value2

obj1 = Airthmatic()

obj1.Accept()

print("Addition is : ",obj1.Addition())
print("Substraction is : ",obj1.Substraction())
print("Multiplication is : ",obj1.Multiplication())
print("Division is : ",obj1.Division())