divisible = lambda x: True if x % 5 == 0 else False
def main():
    Value = int(input("Enter a number:"))
    ret=divisible(Value)
    print(f"{Value} is divisible by 5 : {ret}")
if __name__ == "__main__":
    main()