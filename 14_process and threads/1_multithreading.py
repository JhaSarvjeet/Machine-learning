#Multithreading
#when to use Multithreading
## 1) I/O bound tasks:-Tasks that  spend more time waiting for I/O operationis.(eg.file operation,Network operation )
##2)concurrent execution:-when you want to improve the throughput of your appliaction by  performing multiple operations concurrently.


import threading
import time

# def print_number():
#     for i in range(5):
#         time.sleep(2)
#         print(f"Number:{i}")
# def print_letter():
#     for letter in "abcd":
#         time.sleep(2)
#         print(f"Letter {letter}")
# t=time.time()
# print_number()
# print_letter()
# finishedTime=time.time()-t
# print(finishedTime)


def print_number():
    for i in range(5):
        time.sleep(2)
        print(f"Number:{i} ")
def print_letter():
    for letter in "abcd":
        time.sleep(2)
        print(f"Letter {letter}")


#create two thread
t1=threading.Thread(target=print_number)
t2=threading.Thread(target=print_letter)


t=time.time()
##startthe thread
t1.start()
t2.start()


#wait for the threads to complete
t1.join()
t2.join()

finishedTime=time.time()-t
print(finishedTime)