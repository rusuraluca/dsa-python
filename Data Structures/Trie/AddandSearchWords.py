"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/design-add-and-search-words-data-structure/
"""


class Node:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class WordDictionary:
    """
    Iterative Search
    """
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]

        curr.isEnd = True

    def search(self, word: str) -> bool:
        app = [self.root]
        for c in word:
            new_app = []

            if c == '.':
                for node in app:
                    new_app.extend(node.children.values())
            else:
                for node in app:
                    if c in node.children:
                        new_app.append(node.children[c])
            if not new_app:
                return False

            app = new_app

        for node in app:
            if node.isEnd:
                return True

        return False


class WordDictionary:
    """
    Recursive Search
    """
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]

        curr.isEnd = True

    def search(self, word: str) -> bool:

        def dfs(j, root):
            curr = root

            for i in range(j, len(word)):
                c = word[i]

                if c == ".":
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False

                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]

            return curr.isEnd

        return dfs(0, self.root)
