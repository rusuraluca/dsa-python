"""
This question is asked by Microsoft.
Given an array of strings, return the longest common prefix that is shared amongst all strings.
Note: you may assume all strings only contain lowercase alphabetical characters.

e.g
input:
["colorado", "color", "cold"]
["a", "b", "c"]
["spot", "spotty", "spotted"]
output:
"col"
""
"spot"
"""


# Sorting approach
# Time Complexity: O(n * log n), where n is the number of characters in the string
# Space Complexity: O(1)
# Sort the given set of N strings.
# Compare the first and last string in the sorted array of strings.
# The string with prefix characters matching in the first and last string will be the answer.
def quick_sort(list):
    less = []
    equal = []
    greater = []

    if len(list) > 1:
        pivot = list[0]
        for elem in list:
            if elem < pivot:
                less.append(elem)
            elif elem == pivot:
                equal.append(elem)
            elif elem > pivot:
                greater.append(elem)
        # Don't forget to return something!
        return quick_sort(less) + equal + quick_sort(greater)
    # You need to handle the part at the end of the recursion,
    # when you only have one element in your array, just return the array.
    else:
        return list


def lcp_sorting(arr):
    arr = quick_sort(arr)
    # arr.sort(reverse=False)

    str1 = arr[0]
    str2 = arr[len(arr)-1]

    n1 = len(str1)-1
    n2 = len(str2)-1

    i = 0
    j = 0

    result = ""

    while i <= n1 and j <= n2:
        if str1[i] != str2[j]:
            break
        result += str1[i]
        i += 1
        j += 1

    return result


# Test
a = ["colorado", "color", "cold"]
print(lcp_sorting(a))

a = ["a", "b", "c"]
print(lcp_sorting(a))

a = ["spot", "spotty", "spotted"]
print(lcp_sorting(a))