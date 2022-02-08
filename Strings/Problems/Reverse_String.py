"""
This question is asked by Google.
Given a string, reverse all of its characters and return the resulting string.

e.g.:
input:
“Cat”
“SuPer SumMer”
“civic”

output:
“taC”
"reMmuS rePuS”
“civic”


Remember:
Python string library doesn't support the in-built “reverse()” as done by other python containers like list,
hence knowing other methods to reverse string can prove to be useful.
"""


# Looping through
# We call the function to reverse a string,
# which iterates through every element
# and intelligently join each character in the beginning of a new string
# so as to obtain the reversed string.

# Complexity O(n), n - the number of characters in the string


def reverse_looping(string):
    new_string = ""
    for char in string:
        # add the char at the beginning
        new_string = char + new_string

    return new_string


# Testing
s = "SuPer SumMer"

print("The original string is: ", end="")
print(s)

print("The reversed string (using loops) is: ", end="")
print(reverse_looping(s))


# Recursion approach
# We call the function to reverse a string,
# in which the string is passed as an argument to a recursive function to reverse the string.
# In the function, the base condition is that if the length of the string is equal to 0,
# the string is returned.
# If not equal to 0, the reverse function is recursively called
# to slice the part of the string except the first character
# and concatenate the first character to the end of the sliced string.

def reverse_recursive(string):
    if len(string) == 0:
        return string
    # slice the part of the string except the first character
    # concatenate the first character to the end of the sliced string
    return reverse_recursive(string[1:]) + string[0]


# Testing
s = "SuPer SumMer"

print("The original string is: ", end="")
print(s)

print("The reversed string (using recursion) is: ", end="")
print(reverse_recursive(s))


# Stack approach
# An empty stack is created.
# One by one characters of string are pushed to stack.
# One by one all characters from stack are popped,
# and put them back to string.


# function to create an empty stack
# initializes size of stack as 0
def create_stack():
    stack = []
    return stack


# function to determine the size of the stack
def size(stack):
    return len(stack)


# boolean function to determine if stack is empty
def is_empty(stack):
    if size(stack) == 0:
        return True


# function to add an item to stack
# increases size by 1
def push(stack, char):
    stack.append(char)


# function to remove an item from stack
# decreases size by 1
def pop(stack):
    if is_empty(stack):
        return
    return stack.pop()


def reverse_stacking(string):
    n = len(string)

    stack = create_stack()

    for i in range(0, n, 1):
        push(stack, string[i])

    string = ""

    for i in range(0, n, 1):
        string = string + pop(stack)

    return string


# Testing
s = "SuPer SumMer"

print("The original string is: ", end="")
print(s)

print("The reversed string (using stack) is: ", end="")
print(reverse_stacking(s))


# Extended slice syntax approach
# Extended slice offers to put a “step” field as [start,stop,step],
# and giving no field as start and stop indicates default to 0
# and string length respectively and “-1” denotes starting from end and stop at the start,
# hence reversing string.
def reverse_slice(string):
    string = string[::-1]
    return string


# Testing
s = "SuPer SumMer"

print("The original string is: ", end="")
print(s)

print("The reversed string (using extended slice syntax) is: ", end="")
print(reverse_slice(s))


# Reversed approach
# The reversed() returns the reversed iterator of the given string
# and then its elements are joined empty string separated using join().
# And reversed order string is formed.
def reverse_reversed(string):
    string = "".join(reversed(string))
    return string


# Testing
s = "SuPer SumMer"

print("The original string is: ", end="")
print(s)

print("The reversed string (using reversed) is: ", end="")
print(reverse_reversed(s))
