def Max_number(data):
    max_num = data[0]
    for i in data:
        if i > max_num:
            max_num = i
    return max_num

def main():
    data=[]
    num = int(input("Enter Number of elements : "))
    for i in range(num):
        data.append(int(input("Enter a number : ")))
    result = Max_number(data)
    print("Maximum number is:", result)

if __name__ == "__main__":
    main()
        