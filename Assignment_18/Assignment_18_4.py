def Find_Occurences(data,no):
    count = 0
    for i in data:
        if i == no:
            count +=1
    return count
    
def main():
    data=[]
    num = int(input("Enter Number of elements : "))
    for i in range(num):
        data.append(int(input("Enter a number : ")))
    
    no = int(input("Enter the number to find occurences : "))
    result = Find_Occurences(data,no)
    print(f"Number of occurences of {no} in {data} is : {result}")    
if __name__ == "__main__":
    main()    