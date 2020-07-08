# insertion sort
# cards = [8, 2, 5, 4, 1, 3]


def insertion_sort(list_to_sort):
    # the first element is already in the "sorted side"
    # for all other items, we should do things
    # start at the second item, iterate until the end of array
    for i in range(1, len(list_to_sort)):
        # current number at the index represents the value currently  being sorted
        current_num = list_to_sort[i]
        # move current number back through array (to the sorted side)
        j = i
        # keep moving until it's greater than the number before it, OR , we reach the start
        while j > 0 and current_num < list_to_sort[j - 1]:
            # replace the current value and the one to the left of it
            list_to_sort[j] = list_to_sort[j - 1]
            j -= 1
        # set the value at the current index to the current number
        # at this moment, J representsthe correct new location for the current number we're moving
        list_to_sort[j] = current_num

    return list_to_sort


print(insertion_sort([8, 4, 2, 5, 1, 3]))
