def linear_search(arr, target):
    for num in arr:
        if num == target:
            return num
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    start = 0
    end = (len(arr) - 1)
    found = False

    while end >= start and not found:
        middle_index = (start + end // 2)

        if arr[middle_index] == target:
            return arr[middle_index]
        else:
            if target < arr[middle_index]:
                end = middle_index - 1
            if target > arr[middle_index]:
                start = middle_index + 1
    return -1  # not found
