class Circle:

    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        self.Radius = float(input("Enter Radius of Circle: "))

    def CalculateArea(self):
        self.Area = self.PI * self.Radius * self.Radius
        return self.Area

    def CalculateCircumference(self):
        self.Circumference = 2 * self.PI * self.Radius
        return self.Circumference


# Main
obj1 = Circle()

obj1.Accept()

print("Radius =", obj1.Radius)
print("Area =", obj1.CalculateArea())
print("Circumference =", obj1.CalculateCircumference())