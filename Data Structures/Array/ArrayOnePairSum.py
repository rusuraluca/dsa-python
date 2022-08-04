"""
Array of different numbers.
A given sum.
Find a pair of sum that sums up to the target sum.

Solution:
    1. Naive Solution O(N^2)
        Using two for loops,
        we traverse the array twice
        and check for each element
        if any other element in the array
        adds up to the sum given.
        Not efficient enough.
        Time: O(N^2)
        Space: O(1) constant space

    2. Sorting Solution O(NlogN)
        [-4, -1, 1, 3, 5, 6, 8, 11], 10
            |                   |
            L                   R
        -4 + 11 = 7 - not valid, but 7 < 10 and the numbers are in sorted order
        so we know that we know we should move the left pointer to the right
        -1 + 11 = 10 - valid
        [-4, -1, 1, 3, 5, 6, 8, 11], 13
                       |     |
                       L     R
        -4 + 11 = 7 - not valid, but 7 < 13 and the numbers are in sorted order
        so we know that we know we should move the left pointer to the right
        -1 + 11 = 10 - not valid, but 10 < 13 the same thing
        2 + 11 = 14 > 13, so we move the point at the right to the left
        3 + 8 = 11 < 13, so we move the left
        5 + 8 = 13 = 13 - valid

        We can use an efficient sorting algorithm like Quick Sort
        Time: O(NlogN)
        Space: O(1) - constant time

    3. Hash table Solution O(N)
        This solution may envolve using extra space,
        but it will definitely make our algorithm faster.
        We traverse the array and at each of the numbers that we traverse,
        we check if the number needed to sum up to the target value is stored in the
        hash table.
        targetSum = 10
        currentNum = x
        x + y = 10
        y = 10 - x
        We need to store y in the hash table.
        [3, 5, -4, 8, 11, 1, -1, 6], 10
        {3, 5, -4, 8, 11, 1,
        10 - (-1) = 11 we have it in the array so we return it
        return [11, -1]
        Space/Time Complexity Analysis
        Time: O(N)
        why?
        we traverse the array only once
        and at each number we're just doing calculations (solving for y) which is constant time
        and accesing values in the hash table which is constant time
        Space: O(N)
        why?
        because we are adding values to the hash table, near n
"""


# this function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # if current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# the main function that implements quick_sort
# arr[] --> array to be sorted,
# low  --> starting index,
# high  --> ending index

def quick_sort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


def two_number_sum1(arr, summ):
    for i in range(len(arr) - 1):
        first_num = arr[i]
        for j in range(i+1, len(arr)):
            second_num = arr[j]
            if first_num + second_num == summ:
                return [first_num, second_num]

        return "No pairs found"


def two_number_sum2(arr, summ):
    # quick_sort(arr, 0, len(arr)-1)
    arr.sort()
    l = 0
    r = len(arr)-1
    while l <= r:
        c_sum = arr[l] + arr[r]
        if c_sum > summ:
            r = r-1
        elif c_sum < summ:
            l = l+1
        elif c_sum == summ:
            return arr[l], arr[r]


# with set
def two_number_sum3(arr, summ):
    if len(arr) < 2:
        return "Not enough elements in the array for creating pairs"

    seen = set()
    # for more than one pair:
    # output = set()

    for num in arr:
        target = summ - num
        if target not in seen:
            seen.add(num)
        elif target in seen:
            return target, num
            # output.add((min(num, target), max(num, target)))

    # print'\n'.join(map(str, list(output)))
    return "No pairs in the array"


# with dictionary
def two_number_sum4(arr, summ):
    if len(arr) < 2:
        return "Not enough elements in the array for creating pairs"

    nums = {}
    # for more than one pair:
    # output = set()

    for num in arr:
        target = summ - num
        if target in nums:
            return [target, num]
        else:
            nums[num] = True

    return "No pairs in the array"


arr = [3, 5, -4, 8, 11, 1, -1, 6]
k = 10

print(two_number_sum2(arr, k))
print(two_number_sum3(arr, k))
print(two_number_sum4(arr, k))
