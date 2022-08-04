"""
As move zeros to left, but this time to right ;)
"""


def move_zeros_to_right(array):
    # Edge Case
    if len(array) < 1:
        return array

    idx = 0

    len_arr = len(array) - 1

    for i in range(len_arr):
        if array[i] != 0:
            array[idx] = array[i]
            idx += 1

    while idx < len_arr:
        array[idx] = 0
        idx += 1

    return array


array = [1, 10, 20, 0, 59, 63, 0, 88, 0]
print(move_zeros_to_right(array))

