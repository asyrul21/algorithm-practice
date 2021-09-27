# to understand what Count Inversion is see
# https://www.geeksforgeeks.org/counting-inversions/
# inversions are counted by the sum of inversions of left
# sub array, + sum of inversions of right sub array
# and + the inversions in merge step

# this approach does not modify original array
# but very confusing lol
# avoid this approach

from util import isSorted, testArray2
import time

###########


def _mergeSort(arr):
    invCount = 0
    if(len(arr) > 1):
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]

            invCount += _mergeSort(left)
            invCount += _mergeSort(right)

            i = j = k = 0
            while i < len(left) and j < len(right):
                if(left[i] < right[j]):
                    arr[k] = left[i]
                    i += 1
                else:
                    invCount += (mid - i)
                    arr[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1
            
            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1

    return invCount
   


def mergeSort(arr):
    # declare copy or array
    arrCopy = [item for item in arr]
    inv = _mergeSort(arrCopy)
    return arrCopy, inv



###########
startTime = time.time()
sortedArr, invCounts = mergeSort(testArray2)
endTime = time.time()

print("Initial Array:")
print(testArray2)
print("Sorted Array:")
print(sortedArr)
print("Inversion counts:")
print(invCounts)
print("Sorted: " + str(isSorted(sortedArr)))
print("Execution time:")
print(str(endTime - startTime)+ " ms")
