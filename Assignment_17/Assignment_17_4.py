def Sum_of_factors(n):
    Sum=0
    for i in range(1,n):
        if n % i == 0:
            Sum += i
    return Sum    
    
def main():
    num = int(input("Enter a number: "))
    result = Sum_of_factors(num)
    print(f"The Sum of {num} Factors  is: {result}")
    
if __name__ == "__main__":
    main()    