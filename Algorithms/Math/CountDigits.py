def method1(n: int) -> int:
    """
    Return the length of the string

    convert the integer to a string and get the length of the string.
    """
    # ‘abs’ is used to handle the case even if the number is negative
    return len(str(abs(n)))


def method2(n: int) -> int:
    """
    Return th length by math.log10() function

    Add 1 to the result obtained by math.log() because
    the log of any number is 1 less than
    the number of digits inside that number.
    """
    import math

    return int(math.log10(n) + 1 if n > 0 else (1 if n == 0 else math.log10(-n) + 1))

