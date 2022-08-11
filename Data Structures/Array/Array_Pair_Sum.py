"""
Problem:
    Given an integer array,
    output all the unique pairs that sum up to a specific value k.

For example:
    the input array_pair_sum([1,3,2,2],4)
    would return 2 pairs:
    (1,3)
    (2,2)

NOTE: FOR TESTING PURPOSES CHANGE YOUR FUNCTION SO IT OUTPUTS THE NUMBER OF PAIRS

Solution:
    The O(N) algorithm uses the set data structure.
    We perform a linear pass from the beginning
    and for each element we check
    whether k-element is in the set of seen numbers.
    If it is, then we found a pair of sum k and add it to the output.
    If not, this element doesn't belong to a pair yet,
    and we add it to the set of seen elements.

    The algorithm is really simple once we figure out using a set.
    The complexity is O(N) because we do a single linear scan of the array,
    and for each element we just check whether the corresponding number
    to form a pair is in the set or add the current element to the set.
    Insert and find operations of a set are both average O(1),
    so the algorithm is O(N) in total.
"""


def array_pair_sum(arr, k):

    # Edge Case to check if it doesn't have enough integers for pairs
    if len(arr) < 2:
        return "Not enough elements in the given array"

    # Strategy: Sets for tracking
    # In order to reduce the complexity from O(N^2) to O(N)
    seen = set()
    output = set()

    # For every number in array
    for num in arr:
        # Set target difference
        target = k-num

        # Add it to set if target hasn't been seen
        if target not in seen:
            seen.add(num)
        elif target in seen:
            # Add a tuple with the corresponding pair
            output.add((min(num, target), max(num, target)))

    print('\n'.join(map(str, list(output))))
    return len(output)


print(array_pair_sum([1, 3, 2, 2], 4))
