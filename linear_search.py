import time

def linear_search(arr, target):
    start_time = time.time()
    for i in range(len(arr)):
        if arr[i] == target:
            return time.time() - start_time
    return -1
