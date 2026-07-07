def Addition(num):
    total = 0
    for n in num:
        total += n
    return total

def main():
    data=[]
    num = int(input("Enter Number of elements : "))
    for i in range(num):
        data.append(int(input("Enter a number : ")))
    result = Addition(data)
    print("Addition of all numbers is:", result)

if __name__ == "__main__":
    main()
        