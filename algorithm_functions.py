import time

def selection_sort(arr):
    n = len(arr)
    startTime = time.time()
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    endTime = time.time()
    return arr, endTime - startTime

# Usage:
# my_list = [64, 25, 12, 22, 11]
# selection_sort(my_list)
# print(my_list)

# ----------------------------------------------------------------------------------------------------------------------

def bubble_sort(arr):
    n = len(arr)
    startTime = time.time()
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    endTime = time.time()
    return arr, endTime - startTime

# Usage:
# my_list = [64, 34, 25, 12, 22, 11, 90]
# bubble_sort(my_list)
# print(my_list)

# ----------------------------------------------------------------------------------------------------------------------

def merge_sort(arr):
    startTime = time.time()
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result, endTime - startTime

# Usage:
# my_list = [38, 27, 43, 3, 9, 82, 10]
# sorted_list = merge_sort(my_list)
# print(sorted_list)

# ----------------------------------------------------------------------------------------------------------------------

def quick_sort(arr):
    startTime = time.time()
    if len(arr) <= 1:
        return arr

    pivot = select_pivot(arr)
    less, equal, greater = partition(arr, pivot)

    endTime = time.time()
    return quick_sort(less) + equal + quick_sort(greater), endTime - startTime

def select_pivot(arr):
    return arr[len(arr) // 2]

def partition(arr, pivot):
    less = []
    equal = []
    greater = []

    for element in arr:
        if element < pivot:
            less.append(element)
        elif element == pivot:
            equal.append(element)
        else:
            greater.append(element)

    return less, equal, greater

# Usage:
# my_list = [38, 27, 43, 3, 9, 82, 10]
# sorted_list = quick_sort(my_list)
# print(sorted_list)



