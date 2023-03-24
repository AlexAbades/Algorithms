def merge(arr, l, m, r):
    # Calculate the length of the arrays
    n1 = m - l + 1 # Middle minus the left index + 1 to as it's not inclusive
    n2 = r - m
    # Create empty arrays 
    L = [None] * n1
    R = [None] * n2
    
    # Create data into temporary array, we could do it like that, but at is 
    # only a python property we'll do it a for loop 
    # L1 = arr[:n1]
    # R1 = arr[n2+1:]
    for i in range(n1):  # Running time O(n
        L[i] = arr[l + i]
    for j in range(0, n2):  # Running time O(n)
        R[j] = arr[m + j+ 1]
    # Running time since here O(n + n)
    
    # Now we have to join the arrays in an ordered way 
    i = j = k = 0 
    while i < n1 and j < n2:
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
            k +=1
        else:
            arr[k] = R[j]
            j += 1
            k += 1
    
    # If R is empty 
    while i < n1:  # Running time O(n/2)
        arr[k] = L[i]
        i += 1
        k +=1
        
    # If L is empty 
    while j < n2:  # Running time O(n/2)
        arr[k] = R[j]
        j += 1
        k += 1
    
    # Running time since here O(n + n + n/2 + n/2) = O(3n) = O(n)

#% MergeSort using merge algorithm 

arr = [1, 3, 5, 7, 6, 3, 8]
n = len(arr)

def mergeSort(arr, l, r):
    
    if l < r:
        # Find The middle
        m = l+(r-l)//2 
        
        # If there are arrays of more than one element call again 
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r) 
        #  Runing time recursivity -> O(nlog2n)
        # When l < r ENDs recursevity 
        merge(arr, l, m, r)  # Running time -> O(n)

    # Running time O(n + nlog2n) = O(n)
    print(arr)
mergeSort(arr, 0, n-1)