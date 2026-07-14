class Demo:
    Value = 21      # Class variable

    def __init__(self, No1, No2):
        self.No1 = No1    # Instance variable
        self.No2 = No2

    def Fun(self):
        print("Inside Fun")
        print("No1 =", self.No1)
        print("No2 =", self.No2)

    def Gun(self):
        print("Inside Gun")
        print("No1 =", self.No1)
        print("No2 =", self.No2)
        print("Value =", Demo.Value)


obj1 = Demo(11, 21)
obj2 = Demo(51, 101)

obj1.Fun()
obj2.Fun()
obj1.Gun()
obj2.Gun()