from functools import reduce
maximum = lambda x, y: x if x > y else y

def main():
    data =[]

    n = input("Enter a no of elements:")
    for u in range(int(n)):
        data.append(int(input("Enter a number:")))
    print(data)
    
    ret = reduce(maximum, data)    
    print(f"Maximum of {data} after reduce is : {ret}")

if __name__ == "__main__":
    main()