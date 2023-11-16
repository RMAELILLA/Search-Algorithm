import time

def binary_search(arr, target, low, high):
    start_time = time.time()
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return time.time() - start_time
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
