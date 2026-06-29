def main():
    No = int(input("Enter a number: "))
    original = No
    reverse = 0
    while No > 0:
        digit = No % 10
        reverse = (reverse * 10) + digit
        No //= 10
    if original == reverse:
        print(original, "is a palindrome number.")
    else:
        print(original, "is not a palindrome number.")
                
if __name__ == "__main__":
    main()       
    