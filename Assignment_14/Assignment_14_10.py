Largest_number = lambda x,y,z: x if (x>y and x>z) else (y if (y>x and y>z) else z)
def main():
    Value1 = int(input("Enter first number:"))
    Value2 = int(input("Enter second number:"))
    Value3 = int(input("Enter third number:"))

    ret=Largest_number(Value1,Value2,Value3)
    print(f"Largest of {Value1}, {Value2} and {Value3} is : {ret}")

if __name__ == "__main__":
    main()