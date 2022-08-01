"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/search-a-2d-matrix/


Naive Solution:
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
and so we should definitely try another approach


Binary Search Solution:
-----------------------------------------------
@description:
Treat the matrix as a n*m size 1D matrix (array)
Perform binary search of the array above

@complexity:
Time:  (log(n*m)), for a nxm size matrix
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
        row = len(matrix)
        col = len(matrix[0])
        low = 0
        high = row * col - 1

        while (low <= high):
            mid = (low + high) // 2

            num = matrix[mid // col][mid % col]

            if num == target:
                return True

            elif num < target:
                low = mid + 1

            else:
                high = mid - 1

        return False


class Tests:
    def __init__(self):
        s = Solution()
        assert s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3) == True
        assert s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13) == False


t = Tests()
