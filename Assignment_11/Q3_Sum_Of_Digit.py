def main():
    No = int(input("Enter a number: "))
    sum_of_digits = 0
    while No > 0:
        digit = No % 10
        sum_of_digits += digit
        No //= 10
    print("The sum of digits is:", sum_of_digits)
if __name__ == "__main__":
    main()    
    