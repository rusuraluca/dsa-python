"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/reverse-integer/


Pop and Push Digits & Check before Overflow Solution:
-----------------------------------------------
@description:
We can build up the reverse integer one digit at a time.
While doing so, we can check beforehand whether or not appending another digit would cause overflow.

Reversing an integer can be done similarly to reversing a string.
We want to repeatedly "pop" the last digit off of x and "push" it to the back of the res.
In the end, res will be the reverse of x.

To "pop" and "push" digits without the help of some auxiliary stack/array, we can use math.
//pop operation:
pop = x % 10;
x /= 10;

//push operation:
temp = res * 10 + pop;
res = temp;

However, this approach is dangerous,
because the statement temp = res * 10 + pop can cause overflow.

Luckily, it is easy to check beforehand whether or this statement would cause an overflow.

Lets assume that res is positive.
If temp = res * 10 + pop caused overflow, them it must be that res >= INTMAX/10
If res > INTMAX/10, then temp = res * 10 + pop  will overflow
If res == INTMAX/10, then temp = res * 10 + pop  will overflow if only if pop > 7

Lets assume that res is negative.
If temp = res * 10 + pop caused overflow, them it must be that res <= INTMAX/10
If res < INTMAX/10, then temp = res * 10 + pop  will overflow
If res == INTMAX/10, then temp = res * 10 + pop  will overflow if only if pop < -8

7 and -8 could simply be replaced by INT_MAX%10 and INT_MIN%10

@complexity:
Time:   O(log(x)), where x is the number given, there are roughly log10(x) digits in x
Space:  O(1), no auxiliary space required
"""


class Solution:
    def reverse(self, x: int) -> int:
        num = 0
        a = abs(x)

        while a != 0:
            pop = a % 10
            num = num * 10 + pop
            a = int(a / 10)

        if x > 0 and num < 2 ** 31:
            return num

        elif x < 0 and num <= 2 ** 31:
            return -num

        else:
            return 0


