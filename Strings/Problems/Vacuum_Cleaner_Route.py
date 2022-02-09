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

# Complexity: O(n) - n in the number of moves the robot makes
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

