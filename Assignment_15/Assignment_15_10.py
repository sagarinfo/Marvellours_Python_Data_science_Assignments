count_of_Even = lambda x:True if x % 2 == 0 else False

def main():
    data =[]

    n = input("Enter a no of elements:")
    for u in range(int(n)):
        data.append(int(input("Enter a number:")))
    print(data)
    ret = len(list(filter(count_of_Even, data)))
    print(f"Count of Even numbers in {data} is : {ret}")

if __name__ == "__main__":
    
    main()