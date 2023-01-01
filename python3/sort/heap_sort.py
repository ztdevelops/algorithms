def heap_sort(array):
    n = len(array)

    for i in range(n // 2, -1, -1):
        heapify(array, n, i)
    
    for i in range(n-1, 0, -1):
        # After heapifying, the root will become
        # the largest node. As such, we swap i
        # with index 0 to put the largest node
        # its position.
        array[i], array[0] = array[0], array[1]
        # Heapify again to get the largest node
        # into index 0 again.
        heapify(array, i, 0)

def heapify(array, n, i):
    # Finding the largest node between the current
    # node, its left child, and its right child.
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and array[largest] < array[left]:
        largest = left
    if right < n and array[largest] < array[right]:
        largest = right
    
    # If the largest node is not the current node, then we
    # perform a swap between it and the largest node, and
    # continue heapifying.
    if largest != i:
        array[largest], array[i] = array[i], array[largest]
        heapify(array, n, largest)

print(heap_sort([1, 12, 9, 5, 6, 10]))