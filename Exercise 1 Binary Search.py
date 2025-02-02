def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Example Test Case
numbers = [1, 3, 5, 7, 9, 11, 13]
target = 6
index = binary_search(numbers, target)
if index != -1:
    print(f"Number found at index {index}")
else:
    print(f"Number not found")
