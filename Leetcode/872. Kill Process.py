"""
Problem:
-----------------------------------------------
https://leetcode.com/problems/kill-process/
https://www.lintcode.com/problem/872/?fromId=223&_from=collection


HashMap Solution:
-----------------------------------------------
@description:
We can use a hashmap that stores a particular process value and the list of its direct children.
And then treat it as a tree traversal problem. (BFS/DFS)
or
Construct an adjacency list that maintains the child process linked to that process.
Run BFS by starting with the process to be killed. Store all the processes that are killed


@complexity:
Time:   O(n+e) since we are doing a bfs traversal where n is the number of nodes and e the number of edges
Space:  O(n),  since we store the nodes in a stack/ array
"""


class Solution:
    """
    HashMap Solution:
    """
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        myTree = dict()

        for i, parent in enumerate(ppid):
            myTree[parent] = myTree.get(parent, [])
            myTree[parent].append(pid[i])

        res = []
        stack = [kill]

        while stack:
            cur = stack.pop()
            res.append(cur)
            stack.extend(myTree.get(cur, []))

        return res
