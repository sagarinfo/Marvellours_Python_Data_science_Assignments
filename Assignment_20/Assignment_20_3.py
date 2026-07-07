import time
import threading
def SumEvenList(no):
    Sum = 0
    for i in no:
        if i % 2 == 0:
            Sum =Sum + i
    print("summation of even  :",Sum)
    
def SumOddList(no):
    Sum = 0
    for i in no:
        if i % 2 != 0:
            Sum =Sum + i
    print("summation of of odd  :",Sum)    
        

def main():
    data = [10,23,31,42,77,22,68]
    start_time = time.perf_counter()
    
    t1= threading.Thread(target=SumEvenList,args=(data,))
    t2= threading.Thread(target=SumOddList,args=(data,))
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    end_time = time.perf_counter()
    print(f"Time Required is {end_time - start_time : .4F}")

if __name__ == "__main__":
    main()