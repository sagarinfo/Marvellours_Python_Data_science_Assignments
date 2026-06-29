def main():
    No = int(input("Enter a number: "))
    reverse = 0
    while No > 0:
        digit = No % 10
        reverse = (reverse * 10) + digit
        No //= 10
    print("The reverse of the number is:", reverse)
if __name__ == "__main__":
    main()
    