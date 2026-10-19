# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        LCA in a BST. Time O(h), space O(1).

        The LCA is the first node whose value lies in [low, high],
        where low and high are the smaller and larger of p.val and q.val.
        """
        low = min(p.val, q.val)
        high = max(p.val, q.val)
        node = root

        while node:
            if high < node.val: # both values are smaller -> go left
                node = node.left
            elif low > node.val: # both values are larger -> go right
                node = node.right
            else: # low <= node.val <= high -> split or equality
                return node
        