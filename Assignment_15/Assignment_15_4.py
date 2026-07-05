from functools import reduce
Sum = lambda x, y: x + y

def main():
    data =[]

    n = input("Enter a no of elements:")
    for u in range(int(n)):
        data.append(int(input("Enter a number:")))
    print(data)
    
    ret = reduce(Sum, data)    
    print(f"Sum of {data} after reduce is : {ret}")

if __name__ == "__main__":
    main()