import time 
import threading
def Even_Factors(no):
    Sum=0
    for i in range(2,no,2):    
        if no % i == 0:
            Sum += i
    print("Summation of even no factor",Sum)

def Odd_Factors(no):
    Sum=0
    for i in range(1,no,2):
        if no % i == 0:
            Sum += i
    print("Summation of Odd no factor",Sum)
        

def main():
    
    Start_time =time.perf_counter()
    
    T1 = threading.Thread(target=Even_Factors,args=(12,))

    T2 = threading.Thread(target=Odd_Factors,args=(12,))     
    
    T1.start()
    T2.start()
    
    T1.join()
    T2.join()
    
    end_time = time.perf_counter()
    
    print(f"total time required {Start_time - end_time :.4f}")
    
    stop_threads = True
    print("Exit From main")
    
    
if __name__ == "__main__":
    main()