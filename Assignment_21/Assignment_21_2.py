import threading
import time 
def Maximum(numbers):
    maximum = numbers[0]

    for num in numbers:
        if num > maximum:
            maximum = num

    print("Maximum Number:", maximum)
    


def Minimum(numbers):
    minimum = numbers[0]

    for num in numbers:
        if num < minimum:
            minimum = num

    print("Minimum Number:", minimum)


def main():
    start_time= time.perf_counter()
    numbers = [2, 4, 5, 6, 7, 8, 9, 11, 13, 15, 1, 0]


    t1 = threading.Thread(target=Maximum, args=(numbers,))
    t2 = threading.Thread(target=Minimum, args=(numbers,))

    t1.start()
    t1.join()


    t2.start()
    t2.join()

    end_time = time.perf_counter()
    print(f"Time Required is {end_time - start_time : .4F}") 

    print("Both threads completed")
    
if __name__ == "__main__":
    main()
    