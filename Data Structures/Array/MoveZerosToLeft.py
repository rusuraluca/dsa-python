"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/move-zeroes/


Two Pointers Solution:
-----------------------------------------------
@description:
Take two pointers,
first pointing to the end of the array and the second also to the end.
Traverse once the elements, add at the end the non-zero elements.
Now, the number of zero elements is the difference between the two pointers.
Until they are equal we update the first part of the array with zeros.
Return the array

@complexity:
Time:   O(n), n is the length of the array
Space:  O(1), no auxiliary space required
"""


class Solution:
    def moveZeroesToLeft(self, arr) -> None:
        if len(arr) < 1:
            return arr

        len_arr = len(arr)
        read_index = len_arr - 1
        write_index = len_arr - 1

        while read_index >= 0:
            if arr[read_index] != 0:
                arr[write_index] = arr[read_index]
                write_index -= 1
            read_index -= 1

        while write_index >= 0:
            arr[write_index] = 0
            write_index -= 1

        return arr

