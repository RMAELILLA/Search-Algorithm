import time

def ternary_search(arr, target):
    start_time = time.time()
    low, high = 0, len(arr) - 1

    while low <= high:
        mid1 = low + (high - low) // 3
        mid2 = high - (high - low) // 3

        if arr[mid1] == target:
            elapsed_time = (time.time() - start_time) * 1000  # Convert to milliseconds
            return mid1, elapsed_time  # Return both the index and elapsed time
        elif arr[mid2] == target:
            elapsed_time = (time.time() - start_time) * 1000  # Convert to milliseconds
            return mid2, elapsed_time  # Return both the index and elapsed time
        elif arr[mid1] < target:
            low = mid1 + 1
        elif arr[mid2] > target:
            high = mid2 - 1
        else:
            low, high = mid1 + 1, mid2 - 1

    return -1, (time.time() - start_time) * 1000  # If the target is not found, return -1 and elapsed time
