import sys
sys.setrecursionlimit(5000)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Determine whether subRoot is a subtree of root.

        A subtree is a node of root together with all of its descendants.
        It must match subRoot in both structure and values, down to the leaves.

        Approach:
            1. _are_identical: checks whether two trees are identical.
            2. _contains_subtree: tries every node of root as a starting point,
               using _are_identical at each node.

        Complexity (n = nodes in root, m = nodes in subRoot):
            Time:  O(n * m). There are at most n attempts, and each attempt
                   visits at most m nodes because it stops when subRoot is exhausted.
            Space: O(height_root + height_subRoot) for the recursion stack
                   (worst case O(n + m) for skewed trees).
        """

        def _are_identical(root_node, sub_node):
            """Return True if the trees rooted at both nodes have the same
            structure and values."""
            # Both empty: identical
            if root_node is None and sub_node is None:
                return True
            # Exactly one is empty: the structures differ
            if root_node is None or sub_node is None:
                return False
            # Both exist: compare values first (fails fast on a mismatch),
            # then require identical left and right subtrees
            return (
                root_node.val == sub_node.val
                and _are_identical(root_node.left, sub_node.left)
                and _are_identical(root_node.right, sub_node.right)
            )

        def _contains_subtree(current_node):
            """Return True if any node in the tree rooted at current_node
            is the start of a tree identical to subRoot."""
            # Exhausted this branch without a match
            if current_node is None:
                return False
            # Try the current node as the starting point
            if _are_identical(current_node, subRoot):
                return True
            # Otherwise, a match in the left OR right subtree is enough
            return (
                _contains_subtree(current_node.left)
                or _contains_subtree(current_node.right)
            )

        return _contains_subtree(root)