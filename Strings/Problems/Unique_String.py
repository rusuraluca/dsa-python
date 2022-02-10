"""
This question is asked in the book Cracking the Coding Interview.
Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?

e.g.
input:
"aalex"

output:
False
"""


# Method with dictionary
# Time Complexity: O(n), where n is the number of characters in the string
# Space Complexity: O(n), where n is the number of characters in the string
# Traverse the string one character at a time,
# use a dictionary to store all its characters.
# If a character is added more than once,
# return False.
# If no character is added more than once,
# return True.
def unique_dict(string):
    dict = {}
    for char in string:
        if char in dict:
            return False
        else:
            dict[char] = 1

    return True


# Test
s = "aalex"
print(unique_dict(s))

s = "alex"
print(unique_dict(s))


# Method with hash table
# Time Complexity: O(n), where n is the number of characters in the string
# Space Complexity: O(1)
# Assume the string will contain only ASCII characters.
# Traverse the string one character at a time,
# use a hash table to record which characters have been observed.
# If a character is observed more than once,
# return False.
# If no character is observed more than once
# return True.
# Because we assumed that the string would contain only ASCII characters,
# we can implement the hash table
# as a 128-wide bit vector
# that uses a character's ASCII value as its hash code.
def unique_hashtable(string):
    # hash table as 128 bit vector
    hash_table = [False]*128
    # inspect each element
    for char in string:
        # convert char into its ASCII value
        id = ord(char)
        # check if bit at this ASCII is True -> then we already check it
        if hash_table[id]:
            return False
        # add unobserved char to hash table
        hash_table[id] = True

    return True


# Test
s = "aalex"
print(unique_hashtable(s))

s = "alex"
print(unique_hashtable(s))


# If we cannot use additional structures


# Character comparisons
# Time Complexity: O(n^2), where n is the number of characters in the string
# Space Complexity: O(1)
def unique_comparison(string):
    for i in range(0, len(string)):
        for j in range(0, len(string)):
            if string[i] == string[j] and i != j:
                return False
    return True


# Test
s = "aalex"
print(unique_comparison(s))

s = "alex"
print(unique_comparison(s))


# Sorted comparison
# Time Complexity: O(n*log(n)), where n is the number of characters in the string
# Space Complexity: O(1)
# If we are allowed to modify the original string,
# we could sort it in place in n*log(n) time and test consecutive characters for equality.
def quick_sort(string):
    less = ""
    equal = ""
    greater = ""

    if len(string) > 1:
        pivot = string[0]
        for char in string:
            if char < pivot:
                less = less + char
            elif char == pivot:
                equal = equal + char
            elif char > pivot:
                equal = equal + char
        # Don't forget to return something!
        return quick_sort(less) + equal + quick_sort(greater)
    # You need to handle the part at the end of the recursion,
    # when you only have one element in your array, just return the array.
    else:
        return string


def unique_sorted_comparison(string):
    quick_sort(string)
    for i in range(0, len(string)-1):
        if string[i] == string[i+1]:
            return False

    return True


# Test
s = "xeleeax"
print(unique_sorted_comparison(s))

s = "xael"
print(unique_sorted_comparison(s))
