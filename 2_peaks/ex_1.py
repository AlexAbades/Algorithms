N = int(input())
arr = list(map(int, input().split()))

def peak1(arr,N):
    if arr[0] >= arr[1]:
        print(0)
        return
    for i in range(1,N-2):
        if arr[i-1] <= arr[i] >= arr[i+1]:
            print(i)
            return
    if arr[N-2] <= arr[N-1]:
        print(N-1)
        return

peak1(arr,N)