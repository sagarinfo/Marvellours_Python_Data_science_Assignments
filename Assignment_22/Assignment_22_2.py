import time
import multiprocessing
import os

def Factorial(num):
    print(f"Pid of Factorial : {os.getpid()} PPId of Factorial : {os.getppid()}")
    Fact = []
    for n in range(2,num):
        if num % n == 0:
            Fact.append(n)
    #print(f"Factorial of Number {num} is {n}")
    return Fact     
            
        

def main():
    data = []
    
    n = int(input("Enter a number of Elements : "))
    
    for i in range(n):
        num = int(input("Enter integer : "))
        data.append(num)
    print("input Numbers are : ",data)
    start_time = time.perf_counter()
    pobj = multiprocessing.Pool()
    
    result = pobj.map(Factorial, data)
    
    pobj.close()
    pobj.join()
    end_time = time.perf_counter() 
    
    print("Result of factorial is :")
    print(result)       
    print(f"Required time is : {end_time - start_time :.4f}")
    
if __name__ == "__main__":
    main()