"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/




You can't just take the difference between the highest price and the lowest price,
because the highest price might come before the lowest price.
And you have to buy before you can sell.

What if the price goes down all day?
In that case, the best profit will be negative.

You can do this in O(n) time and O(1) space!


Brute Force:
-----------------------------------------------
The brute force approach would be to try every pair of times
(treating the earlier time as the buy time and the later time as the sell time)
and see which one is higher.
But that will take O(n^2) time,
since we have two nested loops—for every time,
we're going through every other time.
Also, it's not correct: we won't ever report a negative profit! Can we do better?

Well, we’re doing a lot of extra work.
We’re looking at every pair twice.
We know we have to buy before we sell, so in our inner for loop we could just look at every price after the price in our outer for loop.

That could look like this:



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
    def maxProfitBrute(self, stock_prices):
        max_profit = 0

        # Go through every time
        for outer_time in range(len(stock_prices)):

            # For every time, go through every other time
            for inner_time in range(len(stock_prices)):
                # For each pair, find the earlier and later times
                earlier_time = min(outer_time, inner_time)
                later_time = max(outer_time, inner_time)

                # And use those to find the earlier and later prices
                earlier_price = stock_prices[earlier_time]
                later_price = stock_prices[later_time]

                # See what our profit would be if we bought at the
                # earlier price and sold at the later price
                potential_profit = later_price - earlier_price

                # Update max_profit if we can do better
                max_profit = max(max_profit, potential_profit)

        return max_profit

    def maxProfit(self, prices) -> int:
        if not prices or len(prices) is 1:
            return 0

        maxprofit = 0

        for i in range(1, len(prices)):
            # we have a peek
            if prices[i] > prices[i-1]:
                maxprofit += prices[i] - prices[i-1]

        return maxprofit
