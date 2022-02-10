"""
This question is asked by Google.
You are asked to ensure that the first and last names of people begin with a capital letter in their passports.

e.g
input:
"alison heck"
"123p"

output:
"Alison Heck"
"123p"
"""


# Naive Approach
# Time Complexity: O(n), where n is the number of characters in the string
# Space Complexity: O(1)
# Loop through the string,
# find the position of the blank space
# If no blank space is in the string -> Not correct, we return the same string
# else we bring to upper type the char on the position of the blank space +1
# Bring the first char of the string to upper type
def capitalize_simple(string):
    s = 0
    new_string = string[0].upper()
    for i in range(1, len(string)):
        if string[i-1] == ' ':
            s = 1
            new_string = new_string + string[i].upper()
        else:
            new_string = new_string + string[i]

    if s == 0:
        return string

    return new_string


# Test
s = "alison heck"
print(capitalize_simple(s))

s = "123p"
print(capitalize_simple(s))


# Python Approach
# Time Complexity: O(n), where n is the number of characters in the string
# Space Complexity: O(1)
# Split the string in two by string spitting in py
# and use the capitalize() method from python to capitalize the two strings
# Edge case when input is incorrect
# when there's no blank space in the string
def capitalize_py(string):
    if ' ' not in string:
        return string
    for char in string[:].split():
        string = string.replace(char, char.capitalize())
    return string


# Test
s = "alison heck"
print(capitalize_py(s))

s = "paaac"
print(capitalize_py(s))
