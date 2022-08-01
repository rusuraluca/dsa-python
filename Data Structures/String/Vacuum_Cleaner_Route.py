"""
This question is asked by Amazon.
Given a string representing the sequence of moves a robot vacuum makes,
return whether or not it will return to its original position.
The string will only contain L, R, U, and D characters,
representing left, right, up, and down respectively.

e.g.
input:
"LR"
"URURD"
"RUULLDRD"

output:
True
False
True
"""


# Track moves
# Time Complexity: O(n) - where n is the number of moves the robot makes
# Space Complexity: O(1)
# For every move the vacuum makes, there needs to be a "come-back" move
# If it goes once to the left, it must go once to the right in order to come back
# and
# if it goes once up, it must go once down in order to come back
# With 4 variables we keep track of the moves
# and at each step if a "come-back" moves comes we eliminate it from the move
# If in the end all the variables are back to 0, the initialization number
# then the robot comes back to the start
# otherwise it doesn't
def vacuum_cleaner(route):
    left, right, down, up = 0, 0, 0, 0

    for move in route:
        if move == 'L':
            right = right + 1
            left = left - 1
        if move == 'R':
            left = left + 1
            right = right - 1
        if move == 'U':
            down = down + 1
            up = up - 1
        if move == 'D':
            up = up + 1
            down = down - 1

    return left == right == down == up == 0


# Test
s = "LR"
print(vacuum_cleaner(s))
s = "URURDLLD"
print(vacuum_cleaner(s))
s = "RUULLDRD"
print(vacuum_cleaner(s))
