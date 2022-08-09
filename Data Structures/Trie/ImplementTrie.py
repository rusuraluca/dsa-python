"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/implement-trie-prefix-tree/
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
