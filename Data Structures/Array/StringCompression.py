"""
Problem:
    Given a string in the form 'AAAABBBBCCCCCDDEEEE'
    compress it to become 'A4B4C5D2E4'.
    For this problem, you can falsely "compress" strings of single or double letters.
    For instance, it is okay for 'AAB' to return 'A2B1' even though this technically takes more space.

    The function should also be case sensitive, so that a string 'AAAaaa' returns 'A3a3'.

Solution:
    O(N)
    Since Python strings are immutable,
    we'll need to work off of a list of characters,
    and at the end convert that list back into a string with a join statement.
    This solution compresses without checking.
    Known as the RunLength Compression algorithm.
"""


def string_compression(s):
    # Begin Run as empty string
    l = len(s)

    # Edge Case length 0
    if l == 0:
        return ""

    # Edge Case length 1
    if l == 1:
        return s + "1"

    r = ""
    cnt = 1
    i = 1

    while i < l:
        if s[i] == s[i-1]:
            cnt += 1
        else:
            r = r + s[i-1] + str(cnt)
            cnt = 1
        i += 1

    r = r + s[i-1] + str(cnt)

    return r


print(string_compression('ABABBBBCCCCCDdeee'))
