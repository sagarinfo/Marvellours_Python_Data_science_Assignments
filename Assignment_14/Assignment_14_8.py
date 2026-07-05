Adddition = lambda x,y: x+y

def main(): 
    Value1 = int(input("Enter first number:"))
    Value2 = int(input("Enter second number:"))

    ret=Adddition(Value1,Value2)
    print(f"Addition of {Value1} and {Value2} is : {ret}")
if __name__ == "__main__":
    main()    