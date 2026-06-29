def CheckGreater(num1, num2):
    return num1 < num2

def main():
    No1=10
    No2=20
    check = CheckGreater(No1, No2)
    #print("Value of check is:",check)
    if check == True:
        print(No2,"is greater")
if __name__ == "__main__":
    main()  