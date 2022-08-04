"""
Problem
    Consider an array of non-negative integers.
    A second array is formed by shuffling the elements of the first array
    and deleting a random element.
    Given these two arrays, find which element is missing in the second array.

Example:
    Here is an example input,
    the first array is shuffled
    and the number 5 is removed to construct the second array.
    Input:
        finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])
    Output:
        5 is the missing number

Solution
    1. Naive Solution(Brute Forcing it out)
       O(N^2)
            The naive solution is go through every element in the second array
            and check whether it appears in the first array.
            Note that there may be duplicate elements in the arrays
            so we should pay special attention to it.
            The complexity of this approach is O(N^2), since we would need two for loops.

        # Check whether every element in the first array appears in the second array
        for num in arr1:
            if num not in arr2:
                return num

    2. Binary Search Approach
       O(NlogN)
            A more efficient solution is to sort the first array,
            so while checking whether an element in the first array appears in the second,
            we can do binary search.
            But we should still be careful about duplicate elements.
            The complexity of this approach is O(NlogN), since we are using binary search.

    3. Another Approach
       O(NlogN)
            If we don't want to deal with the special case of duplicate numbers,
            we can sort both arrays and iterate over them simultaneously.
            Once two iterators have different values we can stop.
            The value of the first iterator is the missing element.
            The complexity of this approach is also O(NlogN).

        # Sort the arrays
            arr1.sort()
            arr2.sort()

        # Compare elements in the sorted arrays
        # zip - zip matching pairs of the tuples - e.g. zip([1, 2, 3], [4, 5, 6]) -> [(1,4), (2,5), (3,6)]
            for num1, num2 in zip(arr1, arr2):
                if num1 != num2:
                    return num1

        # Otherwise return last element
            return arr1[-1]

    4. HashTable Approach
       O(N)
            In most interviews, you would be expected to come up with a linear time solution.
            We can use a hashtable and store the number of times each element appears in the second array.
            Then for each element in the first array we decrement its counter.
            Once hit an element with zero count that's the missing element.
        # Don't forget to import collections
        import collections

        # Using default dict to avoid key errors
            d = collections.defaultdict(int)

        # Add a count for every instance in array 2
            for num in arr2:
                d[num] += 1

        # Check if a num of array 1 not in dictionary
            for num in arr1:
                if d[num] == 0:
                    return num

                # Otherwise, subtract a count
                else:
                    d[num] -= 1

    5. Sum Approach
       O(N)
        One possible solution is computing the sum of all the numbers in arr1
        and arr2, and subtracting arr2's sum from array1's sum.
        The difference is the missing number in arr2.
        However, this approach could be problematic if the arrays are too long,
        or the numbers are very large.
        Then overflow will occur while summing up the numbers.

        s1 = 0
        s2 = 0
        for num1, num2 in zip(arr1, arr2):
            s1 += num1
            s2 += num2

        return num1-num2

    6. Clever Trick Approach
       O(N)
        By performing a very clever trick,
        we can achieve linear time and constant space complexity without any problems.
        Initialize a variable to 0,
        then XOR every element in the first and second arrays with that variable.
        In the end, the value of the variable is the result,
        missing element in array2.

        XOR - a bit comparison
        A XOR B  =
        0	  0	    0
        0	  1	    1
        1	  0	    1
        1	  1	    0
        If A, B exist or not -> 0
        If one of them exists and the other doesn't -> 0
"""


def find_the_missing_element(arr1, arr2):
    result = 0
    for num in arr1+arr2:
        result ^= num

    return result


print(find_the_missing_element([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6]))
