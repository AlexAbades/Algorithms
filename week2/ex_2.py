N = int(input())
arr = list(map(int,input().split()))

def findmax(arr,N):
    max = 0
    for i in range(N):
        if arr[i] > arr[max]:
            max = i
    print(max)
    # return max

findmax(arr,N)