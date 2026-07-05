Odd_number = lambda x: True if x % 2 != 0 else False

def main():
    Value = int(input("Enter a number:"))
    ret=Odd_number(Value)
    
    print(f"{Value} is odd : {ret}")

if __name__ == "__main__":
    main()    