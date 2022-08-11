"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


Two Pointers Solution:
-----------------------------------------------
@description:
Keep two pointers for the buy and sell day.
Traversing through the array
    Keep track of the current profit
    If the buying is smaller than the selling
        Check if we can update the maximum profit
    Otherwise start from current sell day, i.e. curr buy is curr sell day
    Sell day becomes the next day
Return the maximum profit

@complexity:
Time:   O(n), we traverse once the n characters of the given string
Space:  O(1), no auxiliary space required
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
