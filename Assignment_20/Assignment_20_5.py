import time
import threading  
def Numbers(no):
    for i in range(1,no+1):
        print("numbers are : ",i)
        
def Reversenumbers(no):    
    for i in range(no,1,-1):
        print("reverse no are : ",i)

def main():

    start_time = time.perf_counter()
    
    t1= threading.Thread(target=Numbers,args=(50,))
    t2= threading.Thread(target=Reversenumbers,args=(50,))
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    end_time = time.perf_counter()
    print(f"Time Required is {end_time - start_time : .4F}")

if __name__ == "__main__":
    main()