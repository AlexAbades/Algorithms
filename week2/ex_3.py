N = int(input())
arr = list(map(int,input().split()))

def peak3(arr, i, j):
    m = (i+j)//2

    if m == i:
        if arr[m] >= arr[m-1]:
            return m 
    elif m == j:
        if arr[m] >= arr[m+1]:
            return m 

    if arr[m]>= arr[m+1] and arr[m]>= arr[m-1]:
        return m
    elif arr[m-1] > arr[m]:
        return peak3(arr, i, m-1)
    elif arr[m] < arr[m+1]:
        return peak3(arr, m+1, j)

print(peak3(arr, 0, N))
