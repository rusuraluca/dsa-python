"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/word-break


Brute Force Solution:
-----------------------------------------------
@description:
Use recursion and backtracking.
Check every possible prefix of that string in the dic
    If it is found in the dictionary
        Recursively check the remaingni portion of the string
If in some function call it is found that the complete string is in dic, then return True.

@complexity:
Time:   O(2^n), given a string of length n there are n+1 ways to split it into two parts
              , at each step, we have a choice: to split or not to spit
              , in the wost case when all choices are to be checked, that results in 2^n steps
Space:  O(n), the depth of the recursion tree can go upto n


Trie Solution:
-----------------------------------------------
@description:
We define a list pivots where p is in pivots if and only if wordBreak(s[p:]) == True. We initialize pivots = [len(s)] and traverse s from the back. For each index i we

check if s[i:p] is in wordDict for some p in pivots
if True then we add i at the end of pivots
if False we move on to the next i

Thus s will be breakable into words contained in wordDict if and only if 0 is a pivot (and it should be the last pivot added). So the answer is pivots[-1] == 0.

We define a class Trie as in 208. Implement Trie (Prefix Tree), using nested dictionaries, to be able to search words in wordDict a bit faster. We'll be able to check if a word is in wordDict in O(m) time, where m is the length of the longest word in wordDict. We start by adding every word in wordDict to the trie.


@complexity:
Time:   O(n^3), where n is the length of the input string
              , there are two nested loops, and substring computation at each iteration

Space:  O(n), length of dp array is n+1
"""


class Node:
    def __init__(self):
        # children marks if a node is the end node or not
        self.children = {}

        # is_final marks if a node is the end node or not
        self.is_final = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.is_final = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.is_final

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True


class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        wordTrie = Trie()

        for word in wordDict:
            wordTrie.insert(word)

        n = len(s)
        pivots = [n]

        for i in reversed(range(n)):
            for p in reversed(pivots):
                # True if s[i:p] in wordDict
                if wordTrie.search(s[i:p]):
                    pivots.append(i)
                    break

        return pivots[-1] == 0
