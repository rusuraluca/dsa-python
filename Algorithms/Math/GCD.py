def method1(n: int, m: int) -> int:
    """
    Return gcd by Euclidean Algorithm.
    """
    while m:
        n, m = m, n % m
    return abs(n)


def method2(n: int, m: int) -> int:
    """
    Return gcd by inbuilt gcd() method.
    """
    from math import gcd

    return gcd(n, m)
