def method1(n: int, m: int) -> int:
    """
    This function computes LCM
    calculated from GCD by Euclidean Algorithm.
    """
    def gcd(n: int, m: int) -> int:
        """
        This function computes GCD.
        """
        while m:
            n, m = m, n % m
        return n

    return abs((n * m) // gcd(n, m))


def method2(n: int, m: int) -> int:
    """
    This function computes LCM
    calculated from GCD by inbuilt gcd() method.
    """

    from math import gcd

    return abs(n * m) // gcd(n, m)