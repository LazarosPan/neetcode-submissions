# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """Validate BST using iterative DFS with value bounds."""
        if not root:
            return True

        lowest = float("-inf")
        highest = float("inf")
        stack = [(root, lowest, highest)]

        while stack:
            node, low, high = stack.pop()

            # Every node must satisfy its ancestors' bounds.
            if not low < node.val < high:
                return False

            # Left child inherits the lower bound,
            # but its upper bound becomes the parent's value.
            if node.left:
                stack.append((node.left, low, node.val))

            # Right child inherits the upper bound,
            # but its lower bound becomes the parent's value.
            if node.right:
                stack.append((node.right, node.val, high))

        return True