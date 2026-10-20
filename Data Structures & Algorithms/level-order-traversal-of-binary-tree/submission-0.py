# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        binary tree, left < right
        bfs -> queue, do i need it here?
        visited = []

        tree = no cycles, no need set
        """
        if root == None:
            return []

        visited = []
        queue = deque()
        queue.append(root)

        while queue:
            queue_length = len(queue)
            level = []

            for i in range(queue_length):
                node = queue.popleft()
                
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                
            if level:
                    visited.append(level)
        
        return visited
