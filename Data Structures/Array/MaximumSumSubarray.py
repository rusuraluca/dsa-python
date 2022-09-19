"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/maximum-subarray/


Kadane's Algorithm Solution:
-----------------------------------------------
@description:
The simple idea of Kadane's algorithm is to look for all positive contiguous segments of the array
(max_ending_here is used for this).
And keep track of the maximum sum contiguous segment among all positive segments
(max_so_far is used for this).
Each time we get a positive-sum
compare it with max_so_far and update max_so_far if it is greater than max_so_far

The above algorithm only works if and only if at least one positive number should be present
otherwise it does not work i.e if an array contains all negative numbers it doesn't work

Kadane's Algorithm can be viewed both as greedy and DP.
As we can see that we are keeping a running sum of integers
and when it becomes less than 0, we reset it to 0 (Greedy Part).
This is because continuing with a negative sum is way worse than restarting with a new range.
Now it can also be viewed as a DP, at each stage we have 2 choices:
Either take the current element and continue with the previous sum OR restart a new range.
Both choices are being taken care of in the implementation.

    {-2, -3, 4, -1, -2, 1, 5, -3}

    max_so_far = INT_MIN
    max_ending_here = 0

    for i=0,  a[0] =  -2
    max_ending_here = max_ending_here + (-2)
    Set max_ending_here = 0 because max_ending_here < 0
    and set max_so_far = -2

    for i=1,  a[1] =  -3
    max_ending_here = max_ending_here + (-3)
    Since max_ending_here = -3 and max_so_far = -2, max_so_far will remain -2
    Set max_ending_here = 0 because max_ending_here < 0


    for i=2,  a[2] =  4
    max_ending_here = max_ending_here + (4)
    max_ending_here = 4
    max_so_far is updated to 4 because max_ending_here greater
    than max_so_far which was -2 till now

    for i=3,  a[3] =  -1
    max_ending_here = max_ending_here + (-1)
    max_ending_here = 3

    for i=4,  a[4] =  -2
    max_ending_here = max_ending_here + (-2)
    max_ending_here = 1

    for i=5,  a[5] =  1
    max_ending_here = max_ending_here + (1)
    max_ending_here = 2

    for i=6,  a[6] =  5
    max_ending_here = max_ending_here + (5)
    max_ending_here = 7
    max_so_far is updated to 7 because max_ending_here is
    greater than max_so_far

    for i=7,  a[7] =  -3
    max_ending_here = max_ending_here + (-3)
    max_ending_here = 4

@pseudocode:
Initialize:
    max_so_far = INT_MIN
    max_ending_here = 0

Loop for each element of the array
  (a) max_ending_here = max_ending_here + a[i]
  (b) if(max_so_far < max_ending_here)
            max_so_far = max_ending_here
  (c) if(max_ending_here < 0)
            max_ending_here = 0
Return max_so_far

@complexity:
Time:  O(n)
Space: O(1)


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
    def maxSubArraySum(self, a, size):
        max_so_far = float('-inf')
        max_ending_here = 0

        for i in range(0, size):
            max_ending_here = max_ending_here + a[i]
            if max_so_far < max_ending_here:
                max_so_far = max_ending_here

            if max_ending_here < 0:
                max_ending_here = 0
        return max_so_far


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
