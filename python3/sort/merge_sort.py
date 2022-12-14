'''
Merge sort is a Divide & Conquer algorithm. It divides a large array
into smaller subarrays, and recursively sorts the subarrays.

Steps in Merge Sort
1.  Divide the unsorted array into n subarrays, each of size 1
2.  Repeatedly merge subarrays to produce new, sorted subarrays until
    only one subarray is left, which represents the final sorted array.

Time Complexity: O(n log n)
'''

def merge_sort(array):
    if len(array) == 1:
        return array
    
    mid = len(array) // 2
    
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    res = []
    left_pointer, right_pointer = 0, 0
    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] < right[right_pointer]:
            res.append(left[left_pointer])
            left_pointer += 1
        else:
            res.append(right[right_pointer])
            right_pointer += 1
    
    if left_pointer < len(left):
        res += left[left_pointer:]
    elif right_pointer < len(right):
        res += right[right_pointer:]
    
    return res

unsorted_array = [10, 8, 6, 4, 2, 9, 7, 5, 3, 1]
sorted_array = merge_sort(unsorted_array)