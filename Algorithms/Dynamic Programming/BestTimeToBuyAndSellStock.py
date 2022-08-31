"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


DP Solution:
-----------------------------------------------
@description:
Say the given array is:

[7, 1, 5, 3, 6, 4]

If we plot the numbers of the given array on a graph, we get:

.
                .
        .
                    .
            .

    .
1   2   3   4   5   6

The points of interest are the peaks and valleys in the given graph.
We need to find the largest peak following the smallest valley.
We can maintain two variables - minprice and maxprofit corresponding to the smallest valley and maximum profit
(maximum difference between selling price and minprice) obtained so far respectively.


@complexity:
Time:  O(n), we traverse once the n elements of the array
Space: O(1), no auxiliary space required
"""


class Solution:
    def maxProfit(self, prices) -> int:
        buy = 0
        sell = 1
        max_profit = 0

        while sell < len(prices):
            curr_profit = prices[sell] - prices[buy]

            if prices[buy] < prices[sell]:
                max_profit = max(max_profit, curr_profit)

            else:
                buy = sell

            sell += 1

        return max_profit
