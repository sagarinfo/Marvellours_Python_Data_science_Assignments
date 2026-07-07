def ChkNum(num):
    if num % 2 == 0:
        True
    else:
        False        

def main():
    num = int(input("Enter a number: "))
    if ChkNum(num):
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")
    
if __name__ == "__main__":
    main()    