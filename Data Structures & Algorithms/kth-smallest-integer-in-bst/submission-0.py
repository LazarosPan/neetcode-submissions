# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Return the k-th smallest value (1-indexed) in a BST.

        Approach: iterative in-order traversal (Left -> Node -> Right).
        In a BST, in-order traversal visits keys in ascending order, so the
        k-th node visited is the k-th smallest. Stops early after k visits.

        Time:  O(H + k), H = tree height (O(log n) balanced, O(n) skewed)
        Space: O(H) for the explicit stack
        """
        stack = []        # nodes whose left subtree is still being explored
        curr = root       # current node under inspection

        while curr or stack:
            # Descend as far left as possible; the leftmost node is the
            # smallest unvisited key.
            while curr:
                stack.append(curr)
                curr = curr.left

            # Visit the node on top of the stack (next smallest key).
            curr = stack.pop()
            k -= 1
            if k == 0:            # the k-th visited node is the answer
                return curr.val

            # Node and its left subtree are done; continue in the right subtree.
            curr = curr.right

        # Unreachable under the constraints (1 <= k <= number of nodes).
        raise ValueError("k exceeds the number of nodes in the tree")