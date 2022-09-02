"""
Sieve of Eratosthenes Solution:
@complexity:
Time:   O(n*log(log(n)))
Space:  O(n)
"""


class Solution:
    def countPrimes(self, n: int) -> int:
        # Create a boolean array
        # "prime[0..n]" and initialize
        # all entries it as true.
        # A value in prime[i] will
        # finally be false if i is
        # Not a prime, else true.
        prime = [True for i in range(n)]

        # as 0 & 1 are not prime numbers
        if n < 2:
            return 0
        prime[0], prime[1] = False, False

        p = 2
        while (p * p <= n):
            # If prime[p] is not
            # changed, then it is a prime
            if (prime[p] == True):
                # Update all multiples of p
                for i in range(p * p, n, p):
                    prime[i] = False
            p += 1

        # Count all prime numbers
        return prime.count(True)

        # Count all prime numbers
        count = 0
        for p in range(2, n):
            if prime[p]:
                count += 1
        return count
