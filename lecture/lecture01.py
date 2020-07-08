import random
import time  # we'll use this later

my_range = 500000000
my_size = 1000000

# nums = list(range(0, my_size))

# shuffled_nums = list(range(0, my_size))
# random.shuffle(shuffled_nums)

random_nums = random.sample(range(my_range), my_size)

# print(nums)
# print(shuffled_nums)

num_to_find = 4578


# O(n) linear time


def linear_search(arr, target):
    for num in arr:
        if num == target:
            return True
    return False


print("linear")
start = time.time()
print(linear_search(random_nums, num_to_find))
end = time.time()
print(f"Runtime: {end -  start}")

random_nums.sort()
# print(random_nums)
random_nums = [5, 12, 19, 28, 32, 36, 42, 44, 50, 52, 58, 66, 68, 80, 96]


def binary_search(arr, target):
    start = 0
    end = (len(arr) - 1)

    found = False
    while end >= start and not found:
        # find middle point/index of the array
        middle_index = (start + end) // 2
        # compare the value in the middle with target
        # if the middle value is the same as target, set found to True
        if arr[middle_index] == target:
            found = True
        # move tsart or end index closer to one another, and shrink search space
        else:
            if target < arr[middle_index]:
                end = middle_index - 1
            if target > arr[middle_index]:
                start = middle_index + 1
    return found


print("binary")
start = time.time()
random_nums.sort()
print(binary_search(random_nums, num_to_find))
end = time.time()
print(f"Runtime: {end -  start}")

# print(binary_search(random_nums, 12))
