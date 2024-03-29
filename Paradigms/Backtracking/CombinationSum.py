"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/combination-sum/


Backtracking Solution:
-----------------------------------------------
@description:
Since the problem is to get all the possible results, not the best or the number of result,
thus we don’t need to consider DP (dynamic programming),
backtracking approach using recursion is needed to handle it.

Here is an example of decision tree for the situation when candidates = [2, 3] and target = 6:

                0
              /   \
           +2      +3
          /   \      \
       +2       +3    +3
      /  \     /  \     \
    +2    ✘   ✘   ✘     ✓
   /  \
  ✓    ✘
"""


class Solution:
    def combinationSum(self, candidates, target):
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, nums, target, index, path, res):
        if target < 0:
            return  # backtracking
        if target == 0:
            res.append(path)
            return
        for i in range(index, len(nums)):
            self.dfs(nums, target - nums[i], i, path + [nums[i]], res)

