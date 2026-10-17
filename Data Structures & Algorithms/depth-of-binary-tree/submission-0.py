# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        dfs approach
        compare the len(branch) keep the max or keep a count
        keep a stack to remember which node we are in in order to return and explore the other branches as well.
        when the full tree is explored return the max depth
        """
        if root is None:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return 1+max(left,right)