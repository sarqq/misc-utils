def swap(arr, i, j):
    """
    Utility function
    Swapping two elements in indices i and j
    """
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def heapify(arr, n, i):
    """
    Utility function for Heap sort
    Ensure subtree at index i is a max-heap
    """
    root = i
    left = 2*i + 1      #left child
    right = 2*i + 2     #right child

    #check if children > root
    if left < n and arr[left] > arr[root]:
        root = left
    if right < n and arr[right] > arr[root]:
        root = right
    
    #root not in original index -> swap subtree root and heapify
    if root != i:
        swap(arr, i, root)
        heapify(arr, n, root)

def partition(arr, a, b):
    """
    Utility function for algorithms using partitioning
    """
    pivot = arr[b]
    i = a - 1

    #compare each element to pivot
    #if element <= pivot -> swap
    for j in range(a, b):
        if arr[j] <= pivot:
            i += 1
            swap(arr, i, j)
    
    #sort pivot element into array by swapping
    swap(arr, i + 1, b)
    
    #return partitioning index
    return i + 1

#----------------------------------------------------------

def bubble_sort(arr):
    n = len(arr)

    if n < 2:
        return

    #swap two adjacent elements if not in ascending order
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                swap(arr, j, j+1)


def heap_sort(arr):
    n = len(arr)

    if n < 2:
        return

    #build max-heap w/heapify
    for i in range(n//2, -1, -1):
        heapify(arr, n, i)

    #sort
    for i in range(n-1, 0, -1):
        swap(arr, 0, i)
        heapify(arr, i, 0)


def insertion_sort(arr):
    n = len(arr)

    if n < 2:
        return

    #start at index 1
    for i in range(1, n):
        j = i
        
        #find index j where arr[j] < arr[j-1] 
        while j > 0 and arr[j] < arr[j-1]:
            swap(arr, j, j-1)
            j -= 1


def merge_sort(arr):
    if len(arr) < 2:
        return

    #divide array in half from the middle
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    #sort both subarrays
    merge_sort(left)
    merge_sort(right)

    #merge sorted subarrays
    i = j = k = 0

    #compare equivalent elements in both subarrays, place
    #elements in ascending order into main array
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = left[j]
            j += 1
        k += 1

    #place remaining elements into main array
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


def quicksort(arr, a, b):
    if len(arr) < 2 or a > b:
        return
    
    #find pivot element, such that left < pivot < right
    pivot = partition(arr, a, b)

    #sort
    quicksort(arr, a, pivot-1)
    quicksort(arr, pivot+1, b)


def selection_sort(arr):
    n = len(arr)

    if n < 2:
        return
    
    #find smallest element of array
    for i in range(n):
        min_i = i
        
        for j in range(i+1, n):
            if arr[j] < arr[min_i]:
                min_i = j
        
        #swap smallest element with arr[i]
        swap(arr, i, min_i)


def tree_sort(arr):
    pass

