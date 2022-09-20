"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/next-permutation/


Brute Force Solution:
-----------------------------------------------
@description:
We find out every possible permutation of list formed by the elements of the given array
and find out the permutation which is just larger than the given one.
But this one will be a very naive approach,
since it requires us to find out every possible permutation
which will take really long time and the implementation is complex.
Thus, this approach is not acceptable at all. Hence, we move on directly to the correct approach.

@complexity:
Time:   O(n!), total possible permutations is n!
Space:  O(n), since an array will be used to store the permutations


One-Pass Solution:
-----------------------------------------------
@description:
"""