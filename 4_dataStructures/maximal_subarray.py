N = int(input())
A = list(map(int, input().split()))


# Kadane's Algorithm
# Dynamic Programing
# local_maximum at index "i" is the maximum of A[i] and the sum of A[i] and local_maximum at index i-1.


A = [1, 2, -3, 4, -1, 3, -5]
N = len(A)



def maxsubarr(n, arr):
    local_max = 0 
    global_max = 0 

    for i in range(n):
        local_max = max(arr[i], arr[i] + local_max)
        if local_max > global_max:
            global_max = local_max
        
    return global_max


print(maxsubarr(N,A))