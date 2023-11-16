import time
import random

def linear_search(arr, target):
    start_time = time.time()
    for i in range(len(arr)):
        if arr[i] == target:
            return time.time() - start_time
    return -1

def binary_search(arr, target):
    start_time = time.time()
    low, high = 0, len(arr) - 1
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
        return 0
    i = 1
    n = len(arr)
    while i < n and arr [1] <= target:
        i *= 2
    return binary_search(arr, target, i // 2, min(i, n) - 1)

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

# Add other search algorithms (Interpolation, Ternary) with similar structure

def generate_random_array(size):
    return sorted([random.randint(1, size * 10) for _ in range(size)])

def main():
    data_sizes = [100, 1000, 10000]
    target = 42  # Change this to your target element

    for size in data_sizes:
        data_set = generate_random_array(size)

        linear_time = linear_search(data_set, target)
        binary_time = binary_search(data_set, target)
        exponential_time = exponential_search(data_set, target)
        jump_time = jump_search(data_set, target)
        # Add timing measurements for other search algorithms

        print(f"Data Size: {size}")
        print(f"Linear Search Time: {linear_time} seconds")
        print(f"Binary Search Time: {binary_time} seconds")
        print(f"Exponential Search Time: {exponential_time} seconds")
        print(f"Jump Search Time: {jump_time} seconds")
        # Print timing measurements for other search algorithms

if __name__ == "__main__":
    main()

