def IsPrime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False
def main():
    num = int(input("Enter a number: "))
    if IsPrime(num):
        print(f"{num} is a Prime number")
    else:
        print(f"{num} is not a Prime number")
if __name__ == "__main__":
    main()    