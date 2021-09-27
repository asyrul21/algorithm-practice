# to understand what Count Inversion is see
# https://www.geeksforgeeks.org/counting-inversions/
# inversions are counted by the sum of inversions of left
# sub array, + sum of inversions of right sub array
# and + the inversions in merge step

from util import isSorted, testArray2
import time

###########

# def _mergeSort(arr, start, end):
#    ...


def mergeSort(arr):
    inversionCount = 0

    if(len(arr) > 1):
        mid = len(arr) // 2

        left = arr[:mid]
        right = arr[mid:]

        inversionCount += mergeSort(left)
        inversionCount += mergeSort(right)

        i = j = k = 0

        # merge
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i+= 1
            else:
                # if j < i
                # there will be mid - i + 1 inversions
                inversionCount += (mid - i)
                arr[k] = right[j]
                j+= 1
            k += 1
        
        # check leftout elements
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return inversionCount



###########
startTime = time.time()
invCounts = mergeSort(testArray2)
endTime = time.time()

print("Initial Array:")
print(testArray2)
print("Inversion counts:")
print(invCounts)
print("Sorted: " + str(isSorted(testArray2)))
print("Execution time:")
print(str(endTime - startTime)+ " ms")
