"""
Problem:
    Given two strings, check to see if they are anagrams.
    An anagram is when the two strings can be written using the exact same letters
    (so you can just rearrange the letters to get a different phrase or word).

For example:
    "public relations" is an anagram of "crap built on lies."
    "clint eastwood" is an anagram of "old west action"

Note:
    Ignore spaces and capitalization.
    So "d go" is an anagram of "God" and "dog" and "o d g".

Solution:
    First I thought of three things:
        If two strings have the same frequency of letters/element (meaning each letter shows up the same number of times in both strings)
        then they are anagrams of each other.
        If two strings are equal to each other once they are sorted,
        then they are also anagrams of each other.
        If two strings are not equal then we have am Edge Case
        then they are definitely not anagrams of each other.

    The above sorting approach is simple, but is actually not optimal.
    We should to implement a more manual solution involving
    just counting the number of letters in each string
    to test your ability to understand hash tables.
"""


def anagram(s1, s2):
    # Remove spaces and lowercase letters
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    # Edge Case to check if same number of letters
    if len(s1) != len(s2):
        return False

    # Create counting dictionary
    # (Note could use DefaultDict from Collections module)
    # We'll count the frequency of each letter with the dictionary
    # Then check if all counts are the same
    count = {}

    # Fill dictionary for first string (We will add counts)
    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    # We will do the reverse for the second string
    # Fill dictionary for second string (We will subtract counts)
    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    # Check if all counts are 0
    for k in count:
        if count[k] != 0:
            # If at least one is not, then they are not anagrams
            return False

    # Otherwise they're anagrams
    return True


print(anagram('hi man', 'Hi     man'))
