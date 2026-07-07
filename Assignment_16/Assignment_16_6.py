def CheckNumber(num):
    if num > 0:
        print("Positive Number")
    elif num < 0:
        print("Negative Number")
    else:
        print("Zero")

def main():
    num = int(input("Enter a number: "))
    CheckNumber(num)
    
    
if __name__ == "__main__":
    main()    