"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/


DP Solution:
-----------------------------------------------
@description:
We have to determine the maximum profit that can be obtained by making the transactions
(no limit on the number of transactions done).
For this we need to find out those sets of buying and selling prices which together lead to the maximization of profit.

The key point is we need to consider every peak immediately following a valley to maximize the profit.
In case we skip one of the peaks (trying to obtain more profit),
we will end up losing the profit over one of the transactions leading to an overall lesser profit.

[1, 7, 2, 3, 6, 7, 6, 7]
The graph corresponding to this array would be:

    .               .       .
                .       .


            .
        .
.
1   2   3   4   5   6   7   8

We can see that the sum between
A  = profit between 4 - 3
B  = profit between 5 - 4
C  = profit between 6 - 5
is equal to the difference
D = profit between 6 - 2
So basically the difference between the heights of the consecutive peak and valley.

@complexity:
Time:  O(n), we traverse once the n elements of the array
Space: O(1), no auxiliary space required
"""


class Solution:
    def maxProfit(self, prices) -> int:
        if not prices or len(prices) is 1:
            return 0

        maxprofit = 0

        for i in range(1, len(prices)):
            # we have a peek
            if prices[i] > prices[i-1]:
                maxprofit += prices[i] - prices[i-1]

        return maxprofit
