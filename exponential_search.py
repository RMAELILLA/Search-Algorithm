import time
from binary_search import binary_search

def exponential_search(arr, target):
    start_time = time.time()

    if arr[0] == target:
        elapsed_time = (time.time() - start_time) * 1000  # Convert to milliseconds
        return 0, elapsed_time

    i = 1
    n = len(arr)

    while i < n and arr[i] <= target:
        i *= 2

    result, binary_search_time = binary_search(arr, target, 0, min(i, n) - 1)
    elapsed_time = (time.time() - start_time + binary_search_time) * 1000  # Convert to milliseconds

    return result, elapsed_time
