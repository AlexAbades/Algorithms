from concurrent.futures import process
from time import process_time
import numpy as np 
import matplotlib.pyplot as plt 

def count_time(func):
    times = np.zeros((2,1000))

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    for iter in range(0, 10001,10):
        el_time = 0 
        for aver in range(100):
            x = arr[-1]
            i = 0 
            j = len(arr)

            start = process_time()
            func(arr, i, j, x)
            end = process_time()

            el_time += (end-start)

        el_time /= 100
        # Size of array 
        times[0][iter] = len(arr)                                                                                                                                                                                       
        # Time 
        times[1][iter] = el_time

        arr += list(np.array(arr)+10)

    plt.plot(times)


    


