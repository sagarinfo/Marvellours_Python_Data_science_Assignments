import time
import multiprocessing

def Sum_Squares(num):
    total_sum = 0
    for n in range(2,num + 1,2):
        total_sum = total_sum + n
  
    return total_sum

def main():
    data = []
    
    n = int(input("Enter a number of Elements : "))
    
    for i in range(n):
        num = int(input("Enter integer : "))
        data.append(num)
    
    start_time = time.perf_counter()
    pobj = multiprocessing.Pool()
    
    result = pobj.map(Sum_Squares, data)
    
    pobj.close()
    pobj.join()
    end_time = time.perf_counter() 
    
    print("Result is :")
    print(result)       
    print(f"Required time is : {end_time - start_time :.4f}")
    
if __name__ == "__main__":
    main()