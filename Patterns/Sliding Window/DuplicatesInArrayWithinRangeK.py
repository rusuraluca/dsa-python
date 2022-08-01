"""
Problem:
-----------------------------------------------
Find duplicates within a range ‘k’ in an array.

Input: nums = [5, 6, 8, 2, 4, 6, 9], k = 2
Ouput: False

Input: nums = [5, 6, 8, 2, 2, 6, 9], k = 2
Ouput: True

Input: nums = [5, 6, 8, 8, 8, 6, 9], k = 3
Ouput: True


Sliding Window Solution:
-----------------------------------------------
@description:
Traverse the array
    Add each element to a dictionary with it's position
    If we reach a duplicate in the dictionay and it's distance from the previous occurence is smaller or equal to k
        Return True

Return False

@complexity:
Time:   O(n), n is the number of elements in the array
Space:  O(n), for the dictionary since in the worst case there are no duplicates in the array
"""


class Solution:
    def duplicatesInRange(self, arr, k):
        count = 0
        d = {}

        for i in range(len(arr)):
            # if in dic and the rage is within k
            if arr[i] in d and i - d[arr[i]] <= k:
                return True
            else:
                d[arr[i]] = i

        return False


class Tests:
    def __init__(self):
        s = Solution()
        assert s.duplicatesInRange([5, 6, 8, 2, 4, 6, 9], 2) is False
        assert s.duplicatesInRange([5, 6, 8, 2, 2, 6, 9], 2) is True
        assert s.duplicatesInRange([5, 6, 8, 8, 8, 6, 9], 3) is True


t = Tests()
