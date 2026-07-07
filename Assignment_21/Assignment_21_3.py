import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter

    for i in range(1000):
        lock.acquire()      # Lock
        counter = counter + 1
        lock.release()      # Unlock

threads = []


for i in range(3):
    t = threading.Thread(target=increment)
    threads.append(t)


for t in threads:
    t.start()


for t in threads:
    t.join()

print("Final Counter =", counter)