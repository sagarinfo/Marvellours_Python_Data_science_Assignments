from Airthmetic import Add, Sub, Mult, Div

def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    print(f"The sum of {num1} and {num2} is : {Add(num1, num2)}")
    print(f"The difference of {num1} and {num2} is : {Sub(num1, num2)}")
    print(f"The product of {num1} and {num2} is : {Mult(num1, num2)}")
    print(f"The division of {num1} and {num2} is : {Div(num1, num2)}")
    
if __name__ =="__main__":
    main()    