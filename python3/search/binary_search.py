'''
Binary Search is a searching algorithm used in a sorted array 
by repeatedly dividing the search intervals in half.

Requirements for Binary Search
1.  Arrays must be sorted.

Steps in Binary Search
1.  Let min = 0 and max = len(arr) - 1
2.  Use the middle value between min and max as your search index
3.  If the value at the search index matches the target value,
    return the search index.
4.  Else, if the value at the search index is less than the target
    value, set min to the search index + 1.
5.  Else, if the value at the search index is greater than than the
    target value, set max to the search index - 1.
6.  Restart the process from step 2.

Time Complexity: O(log n)
'''

def binary_search(arr: list, target: int):
    minimum = 0
    maximum = len(arr) - 1
    while minimum <= maximum:
        middle = (minimum + maximum) // 2
        if arr[middle] == target:
            return middle
        elif arr[middle] < target:
            minimum = middle + 1
        else:
            maximum = middle - 1
    return -1

def rbinary_search(arr: list, target: int, l=None, r=None):
    if not (l or r):
        l = 0
        r = len(arr) - 1

    if l > r:
        return -1

    mid = (l + r) // 2
    if arr[mid] > target:
        return rbinary_search(arr, target, l, mid - 1)
    elif arr[mid] < target:
        return rbinary_search(arr, target, mid + 1, r)
    else:
        return mid

if __name__ == '__main__':
    arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    target = 10
    index = rbinary_search(arr, target)
    print(index)
