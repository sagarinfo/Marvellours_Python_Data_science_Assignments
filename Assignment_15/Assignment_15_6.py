from functools import reduce
Minimum = lambda x, y: x if x < y else y

def main():
    data =[]

    n = input("Enter a no of elements:")
    for u in range(int(n)):
        data.append(int(input("Enter a number:")))
    print(data)
    
    ret = reduce(Minimum, data)    
    print(f"Minimum of {data} after reduce is : {ret}")

if __name__ == "__main__":
    main()