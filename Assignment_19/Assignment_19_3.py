from functools import reduce
Fdata = lambda x : x if x >=70 and x <=90 else None

Mdata =lambda x : x+10

Rdata = lambda x,y : x * y

def main():
    data = []
    num = int(input("Enter Number of elements : "))
    for i in range(num):
        data.append(int(input("Enter a number : ")))
    print("List of numbers is : ", data)
    
    result = list(filter(Fdata, data))
    print("Numbers between 70 and 90 are : ", result)
    
    Mresult = list(map(Mdata, result))
    print("Numbers after adding 10 are : ", Mresult)
    
    Rresult = reduce(Rdata, Mresult)
    print("Product of all numbers is : ", Rresult)
        
if __name__ == "__main__":
    main()