"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/combination-sum-ii/


Backtracking Solution:
-----------------------------------------------
@description:
Since the problem is to get all the possible results, not the best or the number of result,
thus we don’t need to consider DP (dynamic programming),
backtracking approach using recursion is needed to handle it.
"""


class Solution:
    def combinationSum2(self, candidates, target):
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, candidates, target, index, path, res):
        if target < 0:
            return  # backtracking
        if target == 0:
            res.append(path)
            return  # backtracking
        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i-1]:
                continue
            self.dfs(candidates, target-candidates[i], i+1, path+[candidates[i]], res)