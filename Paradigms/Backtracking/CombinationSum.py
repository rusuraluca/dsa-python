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
    def combinationSum(self, candidates, target: int, finalCombinations = [], currentCombination = [], startFrom = 0):
        # by adding another candidate we've gone below zero
        # this would mean that the last candidate was not acceptable
        if target < 0:
            return finalCombinations

        if target == 0:
            # if after adding the previous candidate our remaining sum becomes zero
            # we need to save the current combination since it is one of the answers we're looking for
            finalCombinations.append(currentCombination)
            return finalCombinations

        # if we haven't reached zero yet let's continue to add all possible candidates that are left
        for candIdx in range(startFrom, len(candidates)):
            currCand = candidates[startFrom]
            currentCombination.append(currCand)
            self.combinationSum(candidates, target - currCand, finalCombinations, currentCombination, candIdx)

            currentCombination.pop()

        return finalCombinations

