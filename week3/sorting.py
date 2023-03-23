# Insertion sort. 


def insertionsort(A, n:int):
    for i in range(n):
        j = i 
        while j > 0  and (A[j-1] > A[j]):
            print(j)
            A[j-1], A[j] = A[j], A[j-1]
            j = j - 1
    
    return A 

arr =[3,76,1,3,4,8,5]


print(insertionsort(arr, len(arr)))

