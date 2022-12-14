'''
# TODO: Description for Quick Sort.
'''

def quick_sort(array, low, high):
    if low < high:    
        partition_index = partition(array, low, high)
        quick_sort(array, low, partition_index - 1)
        quick_sort(array, partition_index + 1, high)

def partition(array, low, high):
    pivot = array[high]
    partition_index = low - 1

    for i in range(low, high):
        if array[i] <= pivot:
            partition_index += 1

            array[partition_index], array[i] = array[i], array[partition_index]
    array[partition_index+1], array[high] = array[high], array[partition_index+1]
    return partition_index+1

unsorted_array = [10, 8, 6, 4, 2, 9, 7, 5, 3, 1]
quick_sort(unsorted_array, 0, len(unsorted_array) - 1)
print(unsorted_array)