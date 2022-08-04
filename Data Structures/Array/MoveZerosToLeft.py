"""
Given an integer array, move all elements that are 0 to the left
while maintaining the order of other elements in the array.
The array has to be modified in-place.

Runtime complexity: Linear, O(n)O(n)

Memory Complexity: Constant, O(1)O(1)

Keep two markers: read_index and write_index and point them to the end of the array.
Let's take a look at an overview of the algorithm.
    While moving read_index towards the start of the array:

    If read_index points to 0, skip.
    If read_index points to a non-zero value, write the value at read_index to write_index and decrement write_index.
    Assign zeros to all the values before the write_index and to the current position of write_index as well.

read = 8
write = 8

array = [1, 10, 20, 0, 59, 63, 0, 88, 0]
                                      |
                                      is 0 -> yes -> move to the left
                                                  -> read = read - 1 = 7
                                  |
                                  is not 0 -> place it to the write position of the array = 8
                                           -> write = 8 - 1 = 7
array = [1, 10, 20, 0, 59, 63, 0, 88, 88]
                               |
                               is 0 -> yes -> move to the left
                                           -> read = read - 1 = 6
                            |
                            is not 0 -> place it to the write position of the array = 7
                                     -> write = 6
array = [1, 10, 20, 0, 59, 63, 0, 63, 88]
.
.
.

array = [1, 10, 20, 1, 10, 20, 59, 63, 88]
        read = 0
        write = 2

as long as write >= 0 we change the elements from write to 0 (from right to left) to 0
write = 2
array[2] = 0
write = 1
array[1] = 0
write = 0
array [0] = 0

array = [0, 0, 0, 1, 10, 20, 59, 63, 88]
"""


def move_zeros_to_left(array):
    # Edge Case
    if len(array) < 1:
        return array

    len_arr = len(array)
    read_index = len_arr - 1
    write_index = len_arr - 1

    while read_index >= 0:
        if array[read_index] != 0:
            array[write_index] = array[read_index]
            write_index -= 1
        read_index -= 1

    while write_index >= 0:
        array[write_index] = 0
        write_index -= 1

    return array


array = [1, 10, 20, 0, 59, 63, 0, 88, 0]
print(move_zeros_to_left(array))

