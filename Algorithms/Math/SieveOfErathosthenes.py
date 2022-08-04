"""
Print all primes smaller than or equal to n using Sieve of Eratosthenes.
"""


def method1(n: int) -> list:
    """
    Create a boolean array "sieve[0..n]" and initialize
    all entries it as true. A value in sieve[i] will
    finally be false if i is Not a prime, else true.
    """
    if n <= 2:
        return []
    else:
        sieve = [True] * (n + 1)
        for x in range(3, int(n ** 0.5) + 1, 2):
            for y in range(3, (n // x) + 1, 2):
                sieve[(x * y)] = False
    return [2] + [i for i in range(3, n, 2) if sieve[i]]
