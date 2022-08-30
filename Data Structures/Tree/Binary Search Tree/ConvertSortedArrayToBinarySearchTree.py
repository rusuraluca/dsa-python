"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/


Recursive Solution:
-----------------------------------------------
@description:
The elems in the given array are sorted in ascending order and we need to create
a height-balanced binary search tree.
To start populating the binary search tree, we must find the root node first.
As the list is already sorted, it's obvious that the root is the middle element, i.e mid = (len(nums) - 1) // 2.
Then we must set the left and right node by, again, finding the root node which is the middle of the sub array.
This is a recursive pattern.
Therefore we can just use recursion and list slicing to continue finding the middle elem in
the left and right subarray, i.e. nums[:len(nums)//2] and nums[len(nums)//2 + 1 :].
And we stop when our given array is empty.

However, it takes O(n) to slice, making the entire algorithm O(nlogn).
Therefore, we can create a helper function to pass in the bounds of the array instead,
making it O(n).
Since we are passing in bounds, nums will never be None.
We must stop (the base case) when the left pointer is greater than the right pointer
because we know that this is not a valid subtree.
We cannot stop when they are equal because a node with no children is a valid tree.

@complexity:
n is the number of elems in the given array
Time:   O(n), as the helper function is called n times
Space:  O(n), for the recursive stack
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums):
        return self.traversing(nums, 0, len(nums)-1)

    def traversing(self, nums, left, right):
        # base case
        if left > right:
            return None

        mid = (left + right) // 2
        node = TreeNode(nums[mid])
        node.left = self.traversing(nums, left, mid - 1)
        node.right = self.traversing(nums, mid + 1, right)

        return node


class Tests:
    def __init__(self):
        s = Solution()
        nums = [1, 2, 3, 4, 5]
        assert s.sortedArrayToBST(nums).val == 3

        nums = []
        assert s.sortedArrayToBST(nums) is None

        nums = [-10, -3, 0, 5, 9]
        assert s.sortedArrayToBST(nums).val == 0

        nums = [1, 3]
        assert s.sortedArrayToBST(nums).val == 1

        nums = [1]
        assert s.sortedArrayToBST(nums).val == 1


t = Tests()
