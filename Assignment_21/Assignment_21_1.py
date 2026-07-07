import threading
import time 
def get_primes(numbers):
    primes = []

    for num in numbers:
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                primes.append(num)

    print("Prime Numbers:", primes)


def get_non_primes(numbers):
    non_primes = []

    for num in numbers:
        if num < 2:
            non_primes.append(num)
        else:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    non_primes.append(num)
                    break

    print("Non-Prime Numbers:", non_primes)

def main():
    start_time = time.perf_counter()
    numbers = [2, 4, 5, 6, 7, 8, 9, 11, 13, 15, 1, 0]


    t1 = threading.Thread(target=get_primes, args=(numbers,))
    t2 = threading.Thread(target=get_non_primes, args=(numbers,))

    t1.start()

    t1.join()


    t2.start()

    t2.join()
    end_time = time.perf_counter()
    print(f"Time Required is {end_time - start_time : .4F}")

    print("Both threads completed")
    
if __name__ == "__main__":
    main()
        