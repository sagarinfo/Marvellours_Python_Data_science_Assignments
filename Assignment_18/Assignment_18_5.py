def Prime_Number_sum(data):
    total = 0
    for i in data:
        if i > 1:
            is_prime = True
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                total += i
    return total

def main():
    data=[]
    num = int(input("Enter Number of elements : "))
    for i in range(num):
        data.append(int(input("Enter a number : ")))
    result = Prime_Number_sum(data)
    print(f"Sum of prime numbers in {data} is : {result}")   
if __name__ == "__main__":
    main()    