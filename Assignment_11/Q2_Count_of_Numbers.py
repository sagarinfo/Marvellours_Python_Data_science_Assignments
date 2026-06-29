def main():
    No = int(input("Enter a number: "))
    count = len(str(No)) # Count of digits in the number

    print("The count of numbers that divide", No, "is:", count)
    
if __name__ == "__main__":
    main()    