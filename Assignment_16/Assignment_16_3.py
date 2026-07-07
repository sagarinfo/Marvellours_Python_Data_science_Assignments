def Add(No1, No2):
    return No1 + No2

def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = Add(num1, num2)
    print(f"The sum of {num1} and {num2} is {result}")

if __name__ == "__main__":
        main()