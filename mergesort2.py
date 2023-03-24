def mergeSort(arr):
    if len(arr) > 1:

        m = len(arr)//2

        # Split Array in 2 
        L = arr[:m]
        R = arr[m:]

        # Sorting the first half
        mergeSort(L)

        # Sorting the second half
        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1

            else:
                arr[k] = R[j]
                j += 1 
            
            k += 1
        
        # In case Right array finished before 
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        # Case where Left array finishes early
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


arr = [3, 5, 1, 9, 2]

mergeSort(arr)
print(arrcd )