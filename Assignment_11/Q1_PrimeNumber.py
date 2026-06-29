def main():
    No = int(input("Enter a number: "))
    is_prime = True
    if No <= 1:
        is_prime = False
    else:
        for i in range(2, int(No**0.5) + 1):
            if No % i == 0:
                is_prime = False
                break

    if is_prime:
        print(No, "is a prime number.")
    else:
        print(No, "is not a prime number.")

if __name__ == "__main__":
    main()   