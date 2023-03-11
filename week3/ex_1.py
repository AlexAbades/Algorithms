# Binary search 
# Given a sorted array, use binary search to check if an entry it's in that array
from timer import count_time

def binary_search(arr,i ,j ,x):
    if j < i:
        return False 

    m = (i+j)//2 

    if arr[m] == x:
        return True
    
    if arr[m] > x:
        return binary_search(arr, i, m-1, x)
    else: # arr[m] < x
        return binary_search(arr, m+1, j, x)




count_time(binary_search)

    
    


 

 