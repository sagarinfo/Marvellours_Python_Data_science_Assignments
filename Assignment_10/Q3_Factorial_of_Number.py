def main():
    No = int(input("Enter a number: "))
    Factorial = 1
    for i in range(1, No + 1):
        Factorial *= i
    print("The factorial of", No, "is:", Factorial)
if __name__ == "__main__":
    main()            