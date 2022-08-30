"""
https://leetcode.com/problems/online-stock-span

price: [[], [100], [80], [60], [70], [60], [75], [85]]
days :   0    1      2     3     4     5     6    7

stack: [null, 1]
price: []
count: null
return: null

stack: *[null, 1]* [100, 1]
price: [100]
count: 0 + 1
return: 1

stack: [100, 1], [80, 1]
price: [80]
count: 1
return: 1
.
.
.

stack: [100, 1], [80, 1], *[60, 1]*, [70, 2]
price: [70]
count: 1 + 1 = 2
return: 2

stack: [100, 1], [80, 1], [70, 2], [60, 1]
price: [60]
count: 1
return: 1

stack: [100, 1], [80, 1], *[70, 2], [60, 1]*, [75, 4]
price: [75]
count: 1 + 1 + 2 = 4
return: 4

stack: [100, 1], *[80, 1], [75, 4]*, [85, 4]
price: [85]
count: 1 + 4 + 1 = 6
return: 6

Naive Solution:
@description:
Traverse the input price array. For every element being visited,
traverse elements on the left of it and increment the span value of it while elements on the left side are smaller.

@code:
    def StockSpanner(price, n, span):
        span[0] = 1
        for i in range(1, n, 1):
            span[i] = 1
            j = i - 1
            while (j >= 0) and (price[i] >= price[j]):
                span[i] += 1
                j -= 1

@e.g.:
0 1 2 3
0
1 - 0
2 - 1 - 0
3 - 2 - 1 - 0
=> 1+2+3+...+n=n(n+1)/2 => O(n^2) time complexity

@complexity:
Time: O(n^2)
Space: O(n)

Weak, we can do better!
The problem I'm seeing is that the problem would be so easy if the input would be sorted,
but sorting it would just ruing the problem because we are asked to find the maximum number of consecutive days
(starting from today and going backward) for which the stock price was less than or equal to today's price
MARK consecutive, so sorting wouldn't help at all
but some kind of ordering would help
So I'm thinking of using a data structure like a stack
to have some kind of ordering od the elements in order to be able to check the days before really easy.

Stack Solution:
@description:
Traverse the list of prices once,
the count for each day will always be 1,
if it is the first element => push it to the stack
if it's the second element => check if the top of the stack (the previous elements) has a smaller or equal price
    - if true - the count of the second element increases with the count of the previous element
              - pop the previous from the stack we don't need it anymore

    - if false - append the second element to the stack
               - continue

@complexity:
Time: O(n)
Space: O(n)

List Solution:
@description:


@complexity:
Time: O(n), every element of the array is added and removed from the stack at most once
            so there are total 2*n operations at most
            assuming that a stack operation takes O(1) time,
            we can say that the time complexity is O(n)
Space: O(n), in the worst case when all elements are sorted in decreasing order.


Another Solution: (without using stack)
@code:
    def StockSpanner(price, n, span):
        span[0] = 1
        for i in range(1, n):
            counter = 1
            while ((i - counter) >= 0 and price[i] >= price[i - counter]):
                counter += span[i - counter]
            span[i] = counter
"""


class StockSpanner:
    def __init__(self):
        self.span_stack = []

    def next(self, price: int) -> int:
        count = 1

        # while the stack is not empty and the day price before is smaller than our current day price
        while self.span_stack and self.span_stack[-1][0] <= price:
            # add the day count before to our current day count
            count += self.span_stack[-1][1]

            # pop the day price before from the stack
            self.span_stack.pop()

        # append the new price and count to the stack
        self.span_stack.append([price, count])

        return self.span_stack[-1][1]

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)