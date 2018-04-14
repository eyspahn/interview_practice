"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search_attempt1(input_array, value):
    """Your code goes here."""
    init_ind = int(round(len(input_array)/2))
    if value == input_array[init_ind]:
        return init_ind
    elif value < input_array[init_ind]:
        binary_search(input_array[0:init_ind], value)
    elif value > input_array[init_ind]:
        binary_search(input_array[init_ind:0], value)
    else:
        return -1


def binary_search(input_array, value):
    low_ind = 0
    high_ind = len(input_array)-1
    while low_ind<=high_ind:
        mid_ind = int((high_ind - low_ind)/2))
        if input_array[mid_ind] == value:
            return mid_ind
        elif input_array[mid_ind] < value:
            low_ind = mid_ind + 1
        else:
            high_ind = mid_ind - 1
    return -1
