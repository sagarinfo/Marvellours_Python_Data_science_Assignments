def factorial(no):
    Fact=1
    for i in range(1,no+1):
        Fact = Fact * i
        print(Fact)
    return Fact
def main():
    num = int(input("Enter a number: "))
    result = factorial(num)
    print(f"The factorial of {num} is: {result}")
    
if __name__ == "__main__":
    main()    