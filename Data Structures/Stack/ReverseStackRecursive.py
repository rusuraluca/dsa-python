"""
Reverse a stack using recursion
Given a stack, recursively reverse it only using its abstract data type (ADT) standard operations,
i.e., push(item), pop(), peek(), isEmpty(), size(), etc.


Simple Solution:
Hold all items in a call stack until the stack becomes empty.
Then, insert each item in the call stack at the bottom of the stack.

input stack: 1 2 3 4 5
call stack:
input stack: 1 2 3 4
call stack: 5
.
.
.
input stack:
call stack: 5 4 3 2 1

call stack: 4 3 2 1
input stack: 5
call stack: 3 2 1
input stack: 5 4
.
.
.
call stack:
input stack: 5 4 3 2 1

Drawbacks: from call to input stack we need to insert at bottom of the input stack, not at top as per usual

Solution:
@description:
- pop all items from the stack and hold them in the call stack
- when stack is empty, push each item from the call stack in the stack’s top

@complexity:
Time:   O(n^2), n is the total number of elements in the stack
Space:  O(n),   for the call stack

T(n) = T(n-1) + n
     = T(n-2) + (n-1) + n
     = T(n-3) + (n-2) + (n-1) + n
.....
    = 1 + 2 + … + (n-2) + (n-1) + n
    = n×(n+1)/2
    = O(n^2)
"""