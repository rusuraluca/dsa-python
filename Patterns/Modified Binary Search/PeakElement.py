"""
Suppose we have to find the peak element in an array.
The peak element is an element that is greater than its neighbors.
Suppose we have an input array nums, where nums[i] ≠ nums[i+1],
search for a peak element and return its index.
The array can hold multiple peak elements,
in that case return the index to any one of the peak elements.
We can imagine that nums[-1] = nums[n] = -∞.
So if the array is like [1,2,1,3,5,6,4],
the peak elements should be 1 or 5.

To solve this, we will follow these steps −

    low := 0 and high := last index of array,
    n := size of array,
    ans := infinity
    while low <= high
        mid := low + (high - low)/2
        if mid – 1 >= 0 and nums[mid – 1] <= nums[mid],
            then low := mid,
        otherwise
            high := mid - 1
    return low

"""


def find_peak_element(ll):
    low = 0
    high = len(ll)-1

    while low < high:
        mid = low + (high - low+1) // 2
        if mid-1 >= 0 and ll[mid-1] <= ll[mid]:
            low = mid
        else:
            high = mid-1

    return ll[low+1]


ll = [15, 35, 85, 96, 5, 6, 8, 12]
print(find_peak_element(ll))
