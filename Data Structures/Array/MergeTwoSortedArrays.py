"""
Problem:
-----------------------------------------------
https://www.geeksforgeeks.org/merge-two-sorted-arrays-o1-extra-space/


Extra-Space Solution:
-----------------------------------------------
@description:
We can use a new array of size n+m and put all elements of arr1 and arr2 in it, and sort it.
After sorting it, but all the elements in arr1 and arr2.

@complexity:
Time:   O(n*log(n))+O(n)+O(n)
Space:  O(n)


No-Extra-Space Solution:
-----------------------------------------------
@description:
We can think of Iterating in arr1
and whenever we encounter an element that is greater than the first element of arr2, just swap it.
Now rearrange the arr2 in a sorted manner,
after completion of the loop we will get elements of both the arrays in non-decreasing order.

@pseudocode:
1.  Use a for loop in arr1.
2.  Whenever we get any element in arr1 which is greater than the first element of arr2,swap it.
3.  Rearrange arr2.
Repeat the process.

@complexity:
Time:   O(n*m), the worst case occurs when all elements of ar1 are greater than all elements of ar2
Space:  O(1)
"""