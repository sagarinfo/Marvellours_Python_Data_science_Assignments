def DivisibleByFive(num):
    if num % 5 == 0:
        return True
    else:   
        return False
        

def main():
    num = int(input("Enter a number: "))
    ret = DivisibleByFive(num)
    print(ret)
if __name__ == "__main__":
    main()    