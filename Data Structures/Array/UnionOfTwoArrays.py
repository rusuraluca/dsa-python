"""
Problem:
-----------------------------------------------
Given two arrays a[] and b[] of size n and m respectively.
The task is to find union between these two arrays.

Union of the two arrays can be defined as the set containing distinct elements from both the arrays.
If there are repetitions, then only one occurrence of element should be printed in the union.


Hash Set Solution:
-----------------------------------------------
@description:
Union of two arrays we can get with the Set data structure very easily.
Set is a data structure that allows only the distinct elements in it.
So, when we put the elements of both the array into the set
we will get only the distinct elements that are equal to the union operation over the arrays.

@complexity:
Time:   O(m * log(m) + n * log(n)), but O(m + n) in case of Python
        because in python the set built-in method is quite different than that of C++ once,
        Python uses an hash map internally.
Space:  O(m + n), for the set


One-pass Solution:
-----------------------------------------------
@description:
We can improve performance of getUnion method by iterating over both the arrays for index
from 0 to min(n, m)-1 adding all the elements in both the arrays to the set,
and then iterate over the other array with the remaining elements and add them to the set.

@complexity:
Time:   O(max(m,n)), where n and m are arrays' lengths
Space:  O(m + n), where n and m are arrays' lengths
"""


class Solution:
    def getUnion(self, a, n, b, m):
        s = set()

        for i in range(n):
            s.add(a[i])

        for i in range(m):
            s.add(b[i])

        return s

    def getUnion(self, a, n, b, m):
        hs = set()
        if (n < m):
            min = n
        else:
            min = m

        # add elements from both the arrays for
        # index from 0 to min(n, m)-1
        for i in range(0, min):
            hs.add(a[i])
            hs.add(b[i])

        if n > m:
            for i in range(m, n):
                hs.add(a[i])
        else:
            if n < m:
                for i in range(m, n):
                    hs.add(b[i])
