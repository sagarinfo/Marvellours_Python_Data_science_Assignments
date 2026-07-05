Even_number = lambda x: True if x % 2 == 0 else False
def main():
    Value = int(input("Enter a number:"))
    ret=Even_number(Value)
    
    print(f"{Value} is Even : {ret}")

if __name__ == "__main__":
    main()    