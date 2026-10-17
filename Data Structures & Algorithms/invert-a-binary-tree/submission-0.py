# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        tmp = root.left # keep left in memory in tmp var
        root.left = root.right # assign right to left
        root.right = tmp # assign left (from tmp) to right

        # recursive
        self.invertTree(root.right)
        self.invertTree(root.left)
        
        return root