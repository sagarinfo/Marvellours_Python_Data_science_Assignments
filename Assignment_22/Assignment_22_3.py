import time
import multiprocessing
import os

def count_primes(n):
    count = 0

    for num in range(2, n + 1):
        prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                prime = False
                break
        if prime:
            count += 1

    return count                


def main():

    data = []
    
    n = int(input("Enter a number of Elements : "))
    
    for i in range(n):
        num = int(input("Enter integer : "))
        data.append(num)
    
    start_time = time.perf_counter()
    pobj = multiprocessing.Pool()
    
    result = pobj.map(count_primes, data)
    
    pobj.close()
    pobj.join()
    end_time = time.perf_counter() 
    
    for n, c in zip(data, result):
        print(f"Prime count between 1 and {n} = {c}")

    print(f"Required time is : {end_time - start_time :.4f}")
    
if __name__ == "__main__":
    main()