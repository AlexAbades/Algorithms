def merge(arr, i, m, j):

    L = arr[:m]
    R = arr[m:]
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



def mergeSort(arr, i, j):
    if len(arr) > 1:

        m = (i+j) // 2

        # Sorting the first half
        mergeSort(arr, i, m)
        # Sorting the second half
        mergeSort(arr, m+1, j)
        merge(arr, i, m, j)


arr = [3, 5, 1, 9, 2]

mergeSort(arr, 0, len(arr))
print(arr)
