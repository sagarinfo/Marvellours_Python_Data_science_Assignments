from functools import reduce
def prime_check(num):
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False

#Fdata = lambda x : x if prime_check(x) else None
Mdata =lambda x : x*2

Rdata = lambda x,y : x if x > y else y

def main():
    data = []
    num = int(input("Enter Number of elements : "))
    for i in range(num):
        data.append(int(input("Enter a number : ")))
    print("List of numbers is : ", data)
    
    result = list(filter(prime_check, data))
    print("Prime numbers are : ", result)
    
    Mresult = list(map(Mdata, result))
    print("Doubles of prime numbers are : ", Mresult)
    
    Rresult = reduce(Rdata, Mresult)
    print("Maximum of doubles of prime numbers is : ", Rresult)
        
if __name__ == "__main__":
    main()