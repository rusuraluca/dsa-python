"""
Remove duplicate characters in a given string keeping only the first occurrences.
e.g.
input: "tree traversal"
output: "tre avsl"

"tree traversal"

traverse the string

tree traversal

t
set        = t
new_string = t

r
set        = t, s
new_string = tr

e
set        = t, s, e
new_string = tre

e
set        = t, s, e

" "
set        = t, s, e, " "
new_string = tre

a
set        = t, s, e, " ", a

t
set        = t, s, e, " "
new_string = tre a
.
.
.

@complexity:
Time: O(n), n is the number of characters in the given string
Space: O(m), m is the number of unique characters in the given string
"""