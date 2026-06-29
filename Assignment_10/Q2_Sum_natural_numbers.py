def main():
    No = int(input("Enter a number: "))
    Sum = 0
    for i in range(1, No + 1):
        Sum += i
    print("The sum of first", No, "natural numbers is:", Sum)    
if __name__ == "__main__":
    main()