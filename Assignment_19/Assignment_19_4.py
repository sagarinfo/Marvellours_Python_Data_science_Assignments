from functools import reduce
Fdata = lambda x : x if x%2==0 else None

Mdata =lambda x : x**2

Rdata = lambda x,y : x + y

def main():
    data = []
    num = int(input("Enter Number of elements : "))
    for i in range(num):
        data.append(int(input("Enter a number : ")))
    print("List of numbers is : ", data)
    
    result = list(filter(Fdata, data))
    print("Even numbers are : ", result)
    
    Mresult = list(map(Mdata, result))
    print("Squares of even numbers are : ", Mresult)
    
    Rresult = reduce(Rdata, Mresult)
    print("Sum of squares of even numbers is : ", Rresult)
        
if __name__ == "__main__":
    main()