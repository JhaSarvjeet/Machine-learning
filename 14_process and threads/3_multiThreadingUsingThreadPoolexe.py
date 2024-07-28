#multi Threading with Thread Pool Executer
from concurrent.futures import ThreadPoolExecutor
import time

#function to print Number
def print_Number(num):
    time.sleep(1)
    return f"Number : {num}"
numbers=[1,2,3,4,5,8,7,9,4,6,4,6,4,6,2,155,0,5,9,6,4,6,4,65]
inital_time=time.time()
with ThreadPoolExecutor(max_workers=3) as executor:
    result=executor.map(print_Number,numbers)
for number in result:
    print(number)
print(time.time()-inital_time)
