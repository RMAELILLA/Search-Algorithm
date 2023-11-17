import time

def linear_search(arr, target):
    start_time = time.time()
    for i in range(len(arr)):
        if arr[i] == target:
            elapsed_time = (time.time() - start_time) * 1000  # Convert to milliseconds
            return i, elapsed_time
    return -1, -1