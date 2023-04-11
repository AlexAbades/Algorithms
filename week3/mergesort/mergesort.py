# Merge sort: recursivly sort as the slides


def merge(A, i, m, j):
    n1 = m - i + 1
    n2 = j - m - 1
    # Create empty arrayss:
    L = [None] * n1
    R = [None] * n2

    # We have to iterate trhough the Array 
    for e in range(n1):
        L[e] =  A[i+e]
    # Time Complexity O(n)
    for e2 in range(0, n2):
        R[e2] = A[m+e2+1]
    # Time Complexity O(n)

    # Total time complexity: O(n) + O(n) = O(2n) = O(n)
    # Now we have to join the two arrays:

    # Check both arrays
    idxL = idxR = idxG = 0
    while idxL < n1 and idxR < n2:
        if L[idxL] < R[idxR]:
            A[idxG] = L[idxL]
            idxL += 1
            idxG += 1
        else:
            A[idxG] = R[idxR]
            idxR += 1
            idxG += 1
    # Time complexity O(n2) = O(n/2)
    # If Right it´s empty, we just kee p adding the element one by one to the gloab array
    while idxL < n1:
        A[idxG] = L[idxL]
        idxL += 1
        idxG += 1
    # Time complexity O(n2) = O(n/2)

    # If left it's empty we just keep adding elements from rigth one by one to the gloabl array
    while idxR < n2:
        A[idxG] = R[idxR]
        idxR += 1
        idxG += 1
    # Time complexity O(n2) = O(n/2)

    # As only one of the arrays is going to finish before the other one, only one loop we´ll get in the while loop 
    # Time complexity: O(n/2) + O(n/2) = O(n)
    # Total time complexity O(n + n + n/2 + n/2) = O(3n) = O(n)



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
   

        
    
arr = [3, 5, 1, 9, 2]



mergeSort(arr, 0, len(arr))