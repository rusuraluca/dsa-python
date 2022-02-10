"""
This question is asked by Google.
Given a string, return whether or not it uses capitalization correctly.
A string correctly uses capitalization
if
- all letters are capitalized,
- no letters are capitalized,
or
- only the first letter is capitalized.

e.g.
input:
"USA"
"Calvin"
"compUter"
"coding"

output:
true
true
false
true
"""


# Track capitalization
# Time Complexity: O(n) - where n is the number of characters in string
# Space Complexity: O(1)
# Loop through string, one character at a time
# check for the cases of correct capitalization
# We split in 2 cases:
#   - if it starts with upper char:
#           - keep track of the upper and lower char in two variables:
#                   - if the number of upper char is equal to 1 (the one at the beginning)
#                       -> True
#                   - if the number of upper char is equal to the length of the string (the one at the beginning)
#                       -> True
#                   - else
#                       -> False
#   - if it starts with lower char
#           - if we find an upper case char
#               -> False
#           - else
#               -> False
def correct_capitalization(string):
    if string[0].isupper():
        up = 0
        lo = 0
        for char in string:
            if char.isupper():
                up += 1
            else:
                lo += 1

        if up == 1 or up == len(string):
            return True

        return False

    else:
        for char in string:
            if char.isupper():
                return False
        return True


# Test
s = "USA"
print(correct_capitalization(s))

s = "Calvin"
print(correct_capitalization(s))

s = "compUter"
print(correct_capitalization(s))

s = "coding"
print(correct_capitalization(s))
