"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/maximum-subarray/


Sliding Window Solution:
-----------------------------------------------
@complexity:
Time:  O(n)
Space: O(1)


Divide & Conquer Solution:
-----------------------------------------------
@description:
https://leetcode.com/problems/maximum-subarray/discuss/269879/Divide-and-conquer-in-Python

@complexity:
Time:  O(nlog(n))
Space: O(1)


Dynamic Programming Solution:
-----------------------------------------------
Key points of DP is to find DP formula and initial state.
Assume we have dp[i] - maximum sum of subarray that ends at index i
DP formula:     dp[i] = max(dp[i - 1] + nums[i], nums[i])
Initial state：dp[0] = nums[0]

From above DP formula, notice only need to access its previous element at each step.
In this case, we can use two variables,
currMaxSum - maximum sum of subarray that must end with current index i.
maxSum     - global maximum subarray sum
currMaxSum = max(currMaxSum + nums[i], nums[i]
maxSum     = max(currMaxSum, maxSum)


@complexity:
Time:  O(n), we traverse once the n elements of the array
Space: O(1), no auxiliary space required
"""


class Solution:
    def maxSubArray(self, nums) -> int:
        def divideAndConquer(i, j):
            if i == j:
                return nums[i]

            k = (i + j) // 2
            res1 = divideAndConquer(i, k)
            res2 = divideAndConquer(k + 1, j)

            left = leftMax = nums[k]
            for a in range(k - 1, i - 1, -1):
                left += nums[a]
                leftMax = max(left, leftMax)

            right = rightMax = nums[k + 1]
            for a in range(k + 2, j + 1):
                right += nums[a]
                rightMax = max(right, rightMax)

            res3 = leftMax + rightMax
            return max(res1, res2, res3)

        return divideAndConquer(0, len(nums) - 1)

    def maxSubArrayDP(self, nums) -> int:
        n = len(nums)

        dp = [0 for i in range(n)]

        dp[0] = nums[0]

        for i in range(1, n):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])

        return max(dp)

    def maxSubArraySlidingWindow(self, nums) -> int:
        currentSum = nums[0]
        maxSum = nums[0]

        for i in range(1, len(nums)):
            currentSum = max(nums[i], currentSum + nums[i])
            maxSum = max(maxSum, currentSum)

        return maxSum


class Tests:
    def __init__(self):
        s = Solution()
        assert s.maxSubArraySlidingWindow([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
        assert s.maxSubArrayDP([1]) == 1
        assert s.maxSubArray([5, 4, -1, 7, 8]) == 23


t = Tests()
