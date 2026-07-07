def main():
    num = int(input("Enter a number: "))
    count = 0
    while num > 0:
        num //= 10
        count += 1
    print("Count of digits is:", count)
    
if __name__ == "__main__":
    main()    