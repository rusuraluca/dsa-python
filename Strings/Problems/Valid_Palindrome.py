"""
This question is asked by Facebook.
Given a string, return whether or not it forms a palindrome ignoring case and non-alphabetical characters.
Note: a palindrome is a sequence of characters that reads the same forwards and backwards.

e.g.:
input:
"level"
"algorithm"
"A man, a plan, a canal: Panama."

output:
true
false
true
"""


# Iterative method
# Run a loop from starting to length/2
# and check the first character to the last character
# of the string and second to second last one and so on ….
# If any character mismatches, the string will not be a palindrome.
def valid_palindrome_iterative(string):
    for char in string:
        if char in ":., ":
            string = string.replace(char, "")

    string = string.lower()

    size = len(string)

    for i in range(0, size//2):
        if string[i] != string[size-i-1]:
            return False
    return True


# Test
s = "A man, a plan, a canal: Panama."
print(valid_palindrome_iterative(s))


# Recursive method
# This method compares the first and the last element of the string
# and gives the rest of the substring to a recursive call to itself.
def valid_palindrome_recursive(string):
    for char in string:
        if char in ":., ":
            string = string.replace(char, "")

    string = string.lower()

    size = len(string)

    if size < 2:
        return True

    if string[0] == string[size-1]:
        return valid_palindrome_recursive(string[1:size-1])

    else:
        return False


# Test
s = "A man, a plan, a canal: Panama."
print(valid_palindrome_recursive(s))


# Reverse string
# We reverse the string
# and then check if the reverse and the original are the same or not
# We reverse it by using the extended slice syntax
def valid_palindrome_reverse_slice(string):
    for char in string:
        if char in ':., ':
            string = string.replace(char, '')

    string = string.lower()

    return string == string[::-1]


# Test
s = "A man, a plan, a canal: Panama."
print(valid_palindrome_reverse_slice(s))


# Reverse string
# We reverse it by using the reverse method ''.join(reversed(string))
# We reverse the string
# and then check if the reverse and the original are the same or not
# In this method, the user takes a character of string one by one and store it in an empty variable.
# After storing all the characters user will compare both the string and check whether it is palindrome or not.
def valid_palindrome_reversed(string):
    for char in string:
        if char in ':., ':
            string = string.replace(char, '')

    string = string.lower()

    reverse = ''.join(reversed(string))

    return string == reverse


# Test
s = "A man, a plan, a canal: Panama."
print(valid_palindrome_reversed(s))


# One extra variable method
# In this method, the user takes a character of string one by one
# and store it in an empty variable.
# After storing all the characters
# user will compare both the string
# and check whether it is palindrome or not.
def valid_palindrome_variable(string):
    for char in string:
        if char in ":., ":
            string = string.replace(char, "")

    string = string.lower()

    reversed = ''
    for char in string:
        reversed = char + reversed

    return string == reversed


# Test
s = "A man, a plan, a canal: Panama."
print(valid_palindrome_variable(s))





























