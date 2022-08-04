"""
Problem:
    Given a string of words, reverse all the words.

For example:
    Input:
        'This is the best'

    Output:
        'best the is This'

Note:
    As part of this exercise you should remove all leading and trailing whitespace.
    So that inputs such as:
        '  space here'  and 'space here      '
    both become:
        'here space'

Solution:
    1. Python Tricks Approach
        We could take advantage of Python's abilities
        and solve the problem with the use of split()
        and some slicing or use of reversed:

    return " ".join(reversed(s.split()))

    return " ".join(s.split()[::-1])

    2. Manually Approach
        While these are valid solutions,
        in an interview setting you'll have to work out the basic algorithm that is used.
        In this case what we want to do is loop over the text and extract words form the string ourselves.
        Then we can push the words to a "stack" and in the end opo them all to reverse.
"""


def sentence_reversal(s):
    words = []
    length = len(s)
    spaces = [' ']
    i = 0

    while i < length:
        if s[i] not in spaces:
            word_start = i
            while i < length and s[i] not in spaces:
                i += 1
            words.append(s[word_start:i])
        i += 1

    # return " ".join(reversed(words))
    return reverse_array(words)


# Reversing a list using slicing technique
def reverse_array(s):
    return s[::-1]


print(sentence_reversal('This is the best'))
