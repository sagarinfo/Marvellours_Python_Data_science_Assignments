
from functools import reduce
Max_length = lambda x, y: x if len(x) > len(y) else y

def main():
    data = []
    n = input("Enter a no of Strings:")
    for u in range(int(n)):
        data.append(input("Enter a String:"))
    print(data)
    ret = reduce(Max_length, data)
    print(f"Maximum length of string in {data} after reduce is : {ret}")
if __name__ == "__main__":
    main()