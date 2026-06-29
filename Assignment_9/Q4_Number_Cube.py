def Cube(num1):
    return num1**3
def main():
    No=int(input("Enter number:"))
    result = Cube(No)
    print("Cube of",No,"is:",result)
if __name__ == "__main__":
    main()    