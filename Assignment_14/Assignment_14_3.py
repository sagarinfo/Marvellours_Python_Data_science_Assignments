Max_number = lambda x, y: x if x > y else y
def main():
    Value1 = int(input("Enter first number:"))
    Value2 = int(input("Enter second number:"))

    ret=Max_number(Value1,Value2)
    print(f"Maximum of {Value1} and {Value2} is : {ret}")

if __name__ == "__main__":
    main()
    