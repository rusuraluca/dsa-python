"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/rotate-image/


Rotate Groups of Four Cells Solution:
-----------------------------------------------
@description:
Observe how the cells move in groups when we rotate the image.
We can iterate over each group of four cells and rotate them.

@complexity:
Time:   O(m), as each cell is getting read once and written once
Space:  O(1), no auxiliary space required


Reverse on Diagonal and then Reverse Left to Right Solution:
-----------------------------------------------
@description:
The most elegant solution for rotating the matrix is to firstly reverse the matrix around the main diagonal,
and then reverse it from left to right. These operations are called transpose and reflect in linear algebra.
ROTATED = TRANSPOSED +  REVERSED

@complexity:
Time:   O(m), we perform two steps transposing the matrix and then reversing each row
            , both costing O(m)
Space:  O(1), no auxiliary space required
"""


class Solution:
    def rotate(self, matrix) -> None:
        self.transpose(matrix)
        self.reflect(matrix)

    def transpose(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    def reflect(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]

    def rotate2(self, matrix) -> None:
        n = len(matrix[0])

        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                tmp = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
                matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 - i]
                matrix[j][n - 1 - i] = matrix[i][j]
                matrix[i][j] = tmp
