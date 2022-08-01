# Problem definition

# Naive Approach
# The problem can be solved by dividing the matrix into
#    - loops
#    - or squares
#    - or boundaries

# It can be seen that:
#    - the elements of the outer loop are printed first in a clockwise manner
#    - then the elements of the inner loop is printed

# So printing the elements of a loop can be solved using four loops that print all the elements.

# Every ‘for’ loop defines a single direction movement along with the matrix:
# first for loop
# - represents the movement from left to right
# second crawl
# - represents the movement from top to bottom
# third
# - represents the movement from the right to left
# fourth
# - represents the movement from bottom to up


# Better Aproach
# Draw the path that the spiral makes
# We know that the path should turn clockwise:
#   - whenever it would go out of bounds
#   or
#   - into a cell that was previously visited

#  Let the array have R rows and C columns.
#   seen[r] = the cell on the r-th row and c-th column was previously visited
#   current position = (r, c),
#   facing direction di
#   we want to visit R x C total cells


# As we move through the matrix,
# A candidate’s next position is (cr, cc).
#   If the candidate
#   - is in the bounds of the matrix
#   and
#   - unseen
#   Then => it becomes our next position
#
#   Otherwise,
#        => our next position is the one after performing a clockwise turn

class Solution(object):
    def spiralOrderSeen(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # spiral read array
        ans = []

        if len(matrix) == 0:
            return ans

        r = len(matrix)
        c = len(matrix[0])
        seen = [[0 for i in range(c)] for j in range(r)]
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        di = 0
        x = 0
        y = 0

        for i in range(r * c):

            ans.append(matrix[x][y])

            seen[x][y] = True

            cr = x + dr[di]
            cc = y + dc[di]

            # if in bounds
            if (0 <= cr and cr < r and 0 <= cc and cc < c and not(seen[cr][cc])):
                x = cr
                y = cc
            # clock-wise turn
            else:
                di = (di + 1) % 4
                x += dr[di]
                y += dc[di]

        return ans

    def spiralOrder(self, a):
        # ending row index
        m = len(a)

        # ending column index
        n = len(a[0])

        # starting row index
        k = 0

        # starting column index
        l = 0

        # resulting list
        ans = []

        while (k < m and l < n):
            # Print the first row from the remaining rows
            for i in range(l, n):
                ans.append(a[k][i])
            k += 1

            # Print the last column from the remaining columns
            for i in range(k, m):
                ans.append(a[i][n - 1])
            n -= 1

            # Print the last row from the remaining rows
            if (k < m):
                for i in range(n - 1, (l - 1), -1):
                    ans.append(a[m - 1][i])
                m -= 1

            # Print the first column from the remaining columns
            if (l < n):
                for i in range(m - 1, k - 1, -1):
                    ans.append(a[i][l])
                l += 1

        return ans
