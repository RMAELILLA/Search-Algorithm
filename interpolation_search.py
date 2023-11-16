import time

def interpolation_search(arr, target):
    start_time = time.time()
    low, high = 0, len(arr) - 1

    while low <= high and arr[low] <= target <= arr[high]:
        pos = low + ((target - arr[low]) * (high - low) // (arr[high] - arr[low]))

        if arr[pos] == target:
            return time.time() - start_time
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1
