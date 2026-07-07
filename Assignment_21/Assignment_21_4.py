import threading
import time
def calculate_sum(numbers):
    total = 0
    for i in numbers:
        total = total + i
    return total    


def calculate_product(numbers):

    product = 1
    for i in numbers:
        product = product * i
    return  product   


def main():
    start_time= time.perf_counter()
    numbers = [2, 4, 5, 6, 7, 8, 9, 11, 13, 15, 1, 0]


    t1 = threading.Thread(target=calculate_sum, args=(numbers,))
    t2 = threading.Thread(target=calculate_product, args=(numbers,))

    t1.start()
    t1.join()


    t2.start()
    t2.join()
    
    print("sum  of numbers",calculate_product(numbers))
    print("product of numbers",calculate_sum(numbers))
    
    end_time = time.perf_counter()
    
    print(f"Time Required is {end_time - start_time : .4F}")

    print("Both threads completed")
    
if __name__ == "__main__":
    main()
    