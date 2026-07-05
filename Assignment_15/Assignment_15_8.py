divisible = lambda x: True if x % 3 == 0 and x % 5 == 0 else False

def main():
    data =[]

    n = input("Enter a no of elements:")
    for u in range(int(n)):
        data.append(int(input("Enter a number:")))
    print(data)
    
    ret = filter(divisible, data)    
    print(f"Divisible by 3 and 5 of {data} after filter is : {list(ret)}")

if __name__ == "__main__":
    
    main()