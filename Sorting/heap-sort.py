def heap_sort(arr):
    n = len(arr)
    
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr
    
    
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    # Check if left child is larger than root
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    # Check if right child is larger than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    # Swap root if necessary
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def main():
    arr = [5, 2, 9, 1, 5]
    print(heap_sort(arr))


if __name__ == '__main__':
    main()