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
            return i  # Return only the index

    return -1  # If the target is not found, return -1
