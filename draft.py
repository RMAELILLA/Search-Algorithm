import time
import random

def linear_search(arr, target):
    start_time = time.time()
    for i in range(len(arr)):
        if arr[i] == target:
            return time.time() - start_time
    return -1

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

def exponential_search(arr, target):
    start_time = time.time()
    if arr[0] == target:
        return time.time() - start_time
    i = 1
    n = len(arr)
    while i < n and arr[i] <= target:
        i *= 2
    return binary_search(arr, target, 0, min(i, n) - 1)

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
            return time.time() - start_time
            return i

    return -1

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

def ternary_search(arr, target):
    start_time = time.time()
    low, high = 0, len(arr) - 1

    while low <= high:
        mid1 = low + (high - low) // 3
        mid2 = high - (high - low) // 3

        if arr[mid1] == target:
            return time.time() - start_time
        elif arr[mid2] == target:
            return time.time() - start_time
        elif arr[mid1] < target:
            low = mid1 + 1
        elif arr[mid2] > target:
            high = mid2 - 1
        else:
            low, high = mid1 + 1, mid2 - 1

    return -1

def generate_random_array(size):
    return sorted([random.randint(1, size * 10) for _ in range(size)])

def main():
    data_sizes = [100, 1000, 10000]
    target = 42  # Change this to your target element

    for size in data_sizes:
        data_set = generate_random_array(size)

        linear_time = linear_search(data_set, target)
        binary_time = binary_search(data_set, target, 0, len(data_set) - 1)
        exponential_time = exponential_search(data_set, target)
        jump_time = jump_search(data_set, target)
        interpolation_time = interpolation_search(data_set, target)
        ternary_time = ternary_search(data_set, target)

        print(f"Data Size: {size}")
        print(f"Linear Search Time: {linear_time} seconds")
        print(f"Binary Search Time: {binary_time} seconds")
        print(f"Exponential Search Time: {exponential_time} seconds")
        print(f"Jump Search Time: {jump_time} seconds")
        print(f"Interpolation Search Time: {interpolation_time} seconds")
        print(f"Ternary Search Time: {ternary_time} seconds")

if __name__ == "__main__":
    main()
