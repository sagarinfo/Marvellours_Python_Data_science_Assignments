
square = lambda x: x * x

def main():
    n = input("Enter a no of elements:")
    Value = []
    for u in range(int(n)):
        Value.append(int(input("Enter a number:")))
    print(Value)
    ret = list(map(square, Value))
    print(f"Square of {Value} after map  is : {ret}")    
        
if __name__ == "__main__":
    main()