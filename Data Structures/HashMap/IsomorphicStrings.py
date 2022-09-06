"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/isomorphic-strings/


Base Case:
-----------------------------------------------
If len(s) != len(t) => return False


Hash Map Solution:
-----------------------------------------------
@description:
Check base case
Consider two hash maps for the two given strings
st = {}
ts = {}
Traverse the given string s
    We know the element of s and the element of t at this index: se, te

    If se is in st and st[se] is different than te
    or te is in te and ts[te] is different than se
        => return False

    Update the hash map (dictionary)

Return True

s = "foo", t = "bar"
st = {}
ts = {}

0
f
b
st = {f: b}
ts = {b: f}

1
o
a
st = {f: b, o: a}
ts = {b: f, a: o}

2
o
r
o is in st and st[o] is different than r => return False

but if
s = "foo", t = "baa"
2
o
a
o is in st and st[o] is not different than a => contiue

@complexity:
Time:   O(n) = O(len(s)), we traverse once all the characters of the givens string s
Space:  O(sigma) = O(26) = O(1), for the hashtables
        but since we keep only 26 characters for each one we can say is constant space
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        st = {}
        ts = {}

        for i in range(len(s)):
            scurr = s[i]
            tcurr = t[i]

            if (scurr in st and st[scurr] != tcurr) or (tcurr in ts and ts[tcurr] != scurr):
                return False

            st[scurr] = tcurr
            ts[tcurr] = scurr

        return True
