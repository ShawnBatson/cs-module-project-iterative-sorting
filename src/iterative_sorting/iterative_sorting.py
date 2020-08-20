from collections import defaultdict
#
#
#
#
#
#     return array
# # TO-DO:  implement the Bubble Sort function below
# TO-DO: Complete the selection_sort() function below


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i  # set a current
        smallest_index = cur_index  # set a smallest, set it to current
        # TO-DO: find next smallest element
        # (hint, can do in 3 lines)
        for j in range(smallest_index, len(arr)):  # move the pointer through the loop
            if arr[smallest_index] > arr[j]:  # perform the check of larger number
                smallest_index = j  # change index to smallest number
        # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr


def bubble_sort(arr):
    # loop the array with a for loop
    for i in range(len(arr)-1):  # loop over all the elements
        for j in range(0, len(arr)-1):  # each element, check if it is larger than the next
            if arr[j] > arr[j+1]:  # if j is larger than the next,
                # swap them in their place
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# print(bubble_sort(arr1))
'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the
buckets.

What is the time and space complexity of the counting sort algorithm?
'''


# def counting_sort(arr, maximum=None):
#     # for x in arr:
#     #     x += 1

#     return arr
