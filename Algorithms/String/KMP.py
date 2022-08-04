"""
KMP Algorithm for Pattern Searching

Input:  txt[] = "THIS IS A TEST TEXT"
        pat[] = "TEST"
Output: Pattern found at index 10


Input:  txt[] =  "AABAACAADAABAABA"
        pat[] =  "AABA"
Output: Pattern found at index 0
        Pattern found at index 9
        Pattern found at index 12

The KMP matching algorithm uses degenerating property
(pattern having same sub-patterns appearing more than once in the pattern) of the pattern
and improves the worst case complexity to O(n).
The basic idea behind KMP’s algorithm is:
whenever we detect a mismatch (after some matches),
we already know some of the characters in the text of the next window.
We take advantage of this information to avoid matching the characters that we know will anyway match.

Let us consider below example to understand this.
txt = "AAAAABAAABA"
pat = "AAAA"

We compare first window of txt with pat
txt = "AAAAABAAABA"
pat = "AAAA"  [Initial position]
We find a match. This is same as Naive String Matching.

In the next step, we compare next window of txt with pat.
txt = "AAAAABAAABA"
pat =  "AAAA" [Pattern shifted one position]
This is where KMP does optimization over Naive. In this
second window, we only compare fourth A of pattern
with fourth character of current window of text to decide
whether current window matches or not. Since we know
first three characters will anyway match, we skipped
matching first three characters.

Need of Preprocessing?
An important question arises from the above explanation,
how to know how many characters to be skipped. To know this,
we pre-process pattern and prepare an integer array
lps[] that tells us the count of characters to be skipped.



"""