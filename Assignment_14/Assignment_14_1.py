square = lambda x: x ** 2
def main():
    Value = int(input("Enter a number:"))
    ret=square(Value)
    print(f"square of {Value} is : {ret}")

if __name__ == "__main__":
    main()