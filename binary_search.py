import time

def binary_search(arr, target, low, high):
    start_time = time.time()

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            elapsed_time = (time.time() - start_time) * 1000  # Convert to milliseconds
            return mid  # Return only the index
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # If the target is not found, return -1
