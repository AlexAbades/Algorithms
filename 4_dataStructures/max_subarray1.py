N = int(input())
A = list(map(int, input().split()))

# Kadane's Algorithm
# Dynamic Programing
# local_maximum at index "i" is the maximum of A[i] and the sum of A[i] and local_maximum at index i-1.


def maxSubArray(N, array) -> int:
    
    #Check the length of the elements. That could also be done by checking if N == 1
    if N == 1:
        return array[0]

    sum_array = []
    sum_array.append(array[0])
    max_sum = array[0]

    # Exclude the first element as it's already in
    for i in range(1, N):
        sum_array.append(max(sum_array[i-1] + array[i], array[i]))
        max_sum = max(max_sum, sum_array[i])
        

    return max_sum






print(maxSubArray(N,A))



