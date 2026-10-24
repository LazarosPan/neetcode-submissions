"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        clones = [None] * 101              # index = node.val
        clones[node.val] = Node(node.val)
        stack = [node]
        while stack:
            curr = stack.pop()
            for nb in curr.neighbors:
                if clones[nb.val] is None:
                    clones[nb.val] = Node(nb.val)
                    stack.append(nb)
                clones[curr.val].neighbors.append(clones[nb.val])
        return clones[node.val]