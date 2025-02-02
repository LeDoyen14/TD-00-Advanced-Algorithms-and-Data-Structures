def kandane(arr):
    max_sum = arr[0]
    current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum


# Example Test case
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Maximum Subarray sum", kandane(arr))
