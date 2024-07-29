#multiprocessing
#processe that run in parrallel
#when to use:-CPU BOund Task(tasks that are heavy ion CPU usage(eg:-Mathematical computation,data processing ))
#Parrallel Execution :-Multiples cores of the CPu

import multiprocessing
import multiprocessing.process
import time
def squares_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Squares{i*i}")

def cunes_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"cubes{i*i*i}")
if __name__=="__main__":
    #create two process
    p1=multiprocessing.Process(target=squares_numbers)
    p2=multiprocessing.Process(target=cunes_numbers)


    t=time.time()

    #start the process
    p1.start()
    p2.start()
            
    finishedTime=time.time()-t
    #wait for the process to complete
    p1.join()
    p2.join()
    print(finishedTime)