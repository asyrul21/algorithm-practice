testArray = [2 ,3,14, 5, 16, 19, 21, 44, 7, 90, 55, 42]
###
testArray2 = [8, 4, 2, 1] # has 8 inversions # 2  min swaps
testArray3 = [8, 4, 2, 1, 12, 20, 14, 6] # 5  min swaps
testArray4 = [7, 1, 3, 2, 4, 5, 6] # 5  min swaps

def isSorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(0, len(arr) - 1))