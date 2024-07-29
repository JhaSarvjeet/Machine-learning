#multi processing with Process  Pool Executer
from concurrent.futures import ProcessPoolExecutor
import time

def squared_Number(num):
    time.sleep(2)
    return f"square of {num} is {num**2}"
number=[1,2,3,4,5,6,7,8,9]
if __name__=="__main__":
    with ProcessPoolExecutor(max_workers=3) as executor:
        result=executor.map(squared_Number,number)
    for square in result:
        print(square)