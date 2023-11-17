import time
from binary_search import binary_search

def exponential_search(arr, target):
    start_time = time.time()

    if arr[0] == target:
        return 0

    i = 1
    n = len(arr)

    while i < n and arr[i] <= target:
        i *= 2

    result, _ = binary_search(arr, target, 0, min(i, n) - 1)
    elapsed_time = (time.time() - start_time) * 1000

    return result
