"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/powx-n/


Solution:
-----------------------------------------------
@description:
If the number 'x' is 0 => return 0.
Any number greater than 0 raised to the power 0 will return 1.

Case 1: n is even
Suppose we take input as x = 2 & n = 4
So, 2 raised to the power 4 can be written as (2^2 * 2^2)

Case 2: When n is odd.
Lets take another input i.e. x = 2 & n = 5
Here, 2 raised to the power of 5 can be written as (2^2 * 2^2 * 2)

Let us consider a variable p for 2^2
now, as per the problem p = myPow(x, n/2) where x = 2 and n = 4/2

When n is even => return p * p = myPow(x,n/2) * myPow(x,n/2)
When n is odd  => return p * p * x = myPow(x,n/2) * myPow(x,n/2) * x

Case 3: When n is a negative number i.e n < 0
Suppose we take input as x = 2 & n = -1

Any base if it has a negative power, then it results in reciprocal, but with positive power or integer to the base.
So, x ^ (-n) = 1/x^(n)
Hence, we will make the recursive call to the same function, by the taking the functions reciprocal and mutiply the n with (-1).

@complexity:
Time:   O(logn)
Space:  O(1)
"""


class Solution:
    """
    Recursive Solution:
    """

    def myPowRecursive(self, x, n) -> float:
        if not n:
            return 1

        if n < 0:
            # x ^ (-n) = 1/x^(n)
            return 1 / self.myPowRecursive(x, -n)

        if n % 2:
            return x * self.myPowRecursive(x, n - 1)

        return self.myPowRecursive(x * x, n / 2)


    """
    Iterative Solution:
    """
    def myPowIterative(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n

        pow = 1
        while n:
            # check if odd
            if n & 1:
                pow *= x
            x *= x
            # shifts the first operand the specified number of bits to the right.
            n >>= 1

        return pow
