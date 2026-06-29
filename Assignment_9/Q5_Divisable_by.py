def main():
    No=int(input("Enter number:"))
    if No % 5 == 0 & No % 3 == 0:
        print(No,"is divisible by 3 and 5")   
    else:
        print(No,"is not divisible by 3 and 5")

if __name__ == "__main__":
    main()