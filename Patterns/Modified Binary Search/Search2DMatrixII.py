"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/search-a-2d-matrix-ii/


Linear Search Solution:
-----------------------------------------------
@description:
Loop through all the elements in the matrix row-wise
    If the current element is equal to the target => return true
Return false, if we reach the end and don't find the target

@complexity:
Time:  (n*m), for a nxm size matrix
Space: O(1), no auxiliary space needed

@conclusion:
This solution is not very efficient especially for a huge matrix
and so we should definitely try another approach.


Path Solution:
-----------------------------------------------

@complexity:
Time:  (n+m), for a nxm size matrix
Space: O(1), no auxiliary space needed
"""


class Solution(object):

    def searchMatrixNaive(self, matrix, target: int) -> bool:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == target:
                    return True
        return False

    def searchMatrix(self, matrix, target):
        row = 0
        col = len(matrix[0]) - 1

        # while we're still in the matrix
        while row < len(matrix) and col >= 0:

            if matrix[row][col] > target:
                # we want to eliminate
                # all the elements that are greater than our current value
                # meaning all the numbers below it
                # so by moving our column to the left
                col -= 1

            elif matrix[row][col] < target:
                # we want to eliminate
                # all the elements that are smaller than our current value
                # meaning all the numbers above it
                # so by moving our row down
                row += 1

            else:
                # the current element is equal to the target value
                return True

        return False


class Tests:
    def __init__(self):
        s = Solution()
        assert s.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5) is True
        assert s.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20) is False


t = Tests()
