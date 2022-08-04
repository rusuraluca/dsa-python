"""
In this question we'll implement a function root that calculates the nth root of a number.
The function takes a non negative number x and a positive integer n,
and returns the positive nth root of x within an error of 0.001
(i.e. suppose the real root is y, then the error is: |y-root(x,n)| and must satisfy |y-root(x,n)| < 0.001).

Examples:

input:  x = 7, n = 3
output: 1.913

input:  x = 9, n = 2
output: 3

Constraints:
[time limit] 5000ms

[input] float x

0 <= x
[input] integer n

0 < n
[output] float
"""


def nth_root(x, n):
    low = 0
    high = x

    err = 0.001

    mid = float((low + high)/2)

    while abs(mid**n - x) >= err:
        if mid**n > x:
            high = mid
        else:
            low = mid + 1
        mid = (low + high)/2

    return mid


def test_nth_root():
    x = 9
    n = 2
    print(nth_root(x, n))


test_nth_root()
