def method1(n: int) -> bool:
    """
    Return a boolean value to check if
    there exists any factors greater than 1
    by using range()
    """

    return n > 1 and all(n % i for i in range(2, int(n ** 0.5) + 1))


def method2(n: int) -> bool:
    """
    Return a boolean value to check if
    there exists any factors greater than 1
    by using islice() and count() methods of itertools
    """
    from itertools import count, islice

    def prime(n: int) -> bool:
        return n > 1 and all(n % i for i in islice(count(2), int((n) ** 0.5 - 1)))

    return prime(n)


print(method2(2))