import time

def jump_search(arr, target):
    start_time = time.time()
    n = len(arr)
    step = int(n ** 0.5)
    prev, current = 0, 0

    while current < n and arr[current] < target:
        prev = current
        current += step

    for i in range(prev, min(current, n)):
        if arr[i] == target:
            elapsed_time = (time.time() - start_time) * 1000  # Convert to milliseconds
            return i, elapsed_time  # Return both the index and elapsed time

    return -1, (time.time() - start_time) * 1000  # If the target is not found, return -1 and elapsed time
