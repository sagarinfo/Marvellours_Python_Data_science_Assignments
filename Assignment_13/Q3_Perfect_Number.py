def main():
    No = int(input("Enter a number: "))
    sum_of_factors = 0
    for i in range(1, No):
        if No % i == 0:
            sum_of_factors += i
    if sum_of_factors == No:
        print(No, "is a perfect number.")
    else:
        print(No, "is not a perfect number.")
        
if __name__ == "__main__":
    main()      