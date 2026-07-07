import time 
import threading
def Even_numbers(n):
    for i in range(1,n+1):
        
        print(f"Even no are : {i*2}")

def Odd_numbers(n):
   for i in range(0,n+1):
        print(f"Odd no are : {i+1}")
             

def main():
    
    T1 = threading.Thread(target=Even_numbers,args=(10,))
    
    T2 = threading.Thread(target=Odd_numbers,args=(10,))     
    
    T1.start()
    T2.start()
    
    T1.join()
    T2.join()
    
if __name__ == "__main__":
    main()