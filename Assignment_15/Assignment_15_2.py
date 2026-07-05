CheckEven = lambda x: True if x % 2 == 0 else False

def main():
    n = input("Enter a no of elements:")
    Value = []
    for u in range(int(n)):
        Value.append(int(input("Enter a number:")))
    print(Value)
    ret = list(filter(CheckEven, Value))
    print(f"Even numbers in {Value} after filter are : {ret}")    

if __name__ == "__main__":
    main()