# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Find the lowest common ancestor (LCA) of p and q in a BST.

        Approach:
            In a BST, every value in a node's left subtree is smaller than the
            node, and every value in its right subtree is larger. The LCA is
            therefore the first node, starting at the root, where p and q
            stop being on the same side:
              - both smaller than node.val -> LCA is in the left subtree
              - both larger than node.val  -> LCA is in the right subtree
              - otherwise (split, or node equals p or q) -> node is the LCA

        Args:
            root: root of the BST (all values unique).
            p, q: two distinct nodes guaranteed to exist in the tree.

        Returns:
            The LCA node. A node counts as its own descendant.

        Complexity:
            Time:  O(h), where h is the tree height (O(log n) balanced,
                   O(n) skewed). At most one node per level is visited.
            Space: O(1). The loop keeps no stack, unlike recursion, which
                   uses O(h) call-stack frames.
        """
        node = root  # current node, starting at the root

        # No `node is None` check is needed inside the loop: p and q exist,
        # so we always stop at or above the shallower of the two. The loop
        # condition is only a safeguard for an empty tree.
        while node:
            # Signed differences from the current node:
            #   same sign (product > 0)  -> p and q are on the same side
            #   opposite signs (< 0)     -> p and q are split across node
            #   one is zero (== 0)       -> node is p or q itself
            # The last two cases make node the LCA.
            if (p.val - node.val) * (q.val - node.val) <= 0:
                return node

            # Here both values are on the same side, so comparing p alone
            # is enough to choose the direction.
            node = node.left if p.val < node.val else node.right

        return None  # only reachable for an empty tree