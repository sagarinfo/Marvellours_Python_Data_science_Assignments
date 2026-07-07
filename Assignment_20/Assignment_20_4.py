
import time
import threading

def Small(name):
    print(f"Thread of t1 id is",threading.get_ident())
    count=0
    for i in name:
        if(i.islower()):
            count+=1
    print("Count of small letters are : ",count)        
    
def Capital(name):
    print(f"Thread of t2 id is",threading.get_ident())
    count=0
    for i in name:
        if(i.isupper()):
            count+=1
    print("Count of Capitals letters are : ",count)
def Digit(name):
    print(f"Thread of t3 id is",threading.get_ident())
    count=0
    for i in name:
        if(i.isdigit()):
            count+=1
    print("Count of Digits are : ",count)      

def main():

    name = input("Enter a word with capital, small letters with some digits : ")
    Small(name)
    Capital(name)
    Digit(name)
    
    start_time = time.perf_counter()
    
    t1= threading.Thread(target=Small,args=(name,))
    t2= threading.Thread(target=Capital,args=(name,))
    t3= threading.Thread(target=Capital,args=(name,))
    
    t1.start()
    t2.start()
    t3.start()
    
    end_time = time.perf_counter()
    
    print(f"Time Required is {end_time - start_time : .4F}")

if __name__ == "__main__":
    main()    