import time
import multiprocessing
import os

def count_of_even_numbers(num):
    count = 0
    for n in range(2,num + 1,2):
        count+=1
  
    return count

def main():
    
    data = []
    
    n = int(input("Enter a number of Elements : "))
    
    for i in range(n):
        num = int(input("Enter integer : "))
        data.append(num)
    print("Process ID : ",os.getpid())    
    print("Input numbers are : ",data)
    
    start_time = time.perf_counter()
    pobj = multiprocessing.Pool()
    
    result = pobj.map(count_of_even_numbers, data)
    
    pobj.close()
    pobj.join()
    end_time = time.perf_counter() 
    
    print("Even number Count :")
    print(result)       
    print(f"Required time is : {end_time - start_time :.4f}")
    
if __name__ == "__main__":
    main()