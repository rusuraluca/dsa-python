"""
Problem:
    Given a string, determine if it is composed of all unique characters.
    For example, the string 'abcde' has all unique characters and should return True.
    The string 'aabcde' contains duplicate characters and should return false.

Solution:
    We have two possible solutions.

    1. Using a built-in data structure and a built in function

    2. Using a built-in data structure but using a look-up method to check if the characters are unique.
"""


def unique_characters1(s):
    return len(set(s)) == len(s)


def unique_characters2(s):
    chars = set()
    for let in s:
        # Check if in set
        if let in chars:
            return False
        else:
            chars.add(let)

    return True


print(unique_characters1('ab'))
print(unique_characters2('ab'))
