Cube = lambda x : x ** 3
def main():
    Value = int(input("Enter a number:"))
    ret=Cube(Value)
    print(f"Cube of {Value} is : {ret}")

if __name__ == "__main__":
    main()    