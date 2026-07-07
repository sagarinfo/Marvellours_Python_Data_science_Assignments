def Min_number(data):
    min_num = data[0]
    for i in data:
        if i < min_num:
            min_num = i
    return min_num

def main():
    data=[]
    num = int(input("Enter Number of elements : "))
    for i in range(num):
        data.append(int(input("Enter a number : ")))
    result = Min_number(data)
    print("Minimum number is:", result)

if __name__ == "__main__":
    main()
        