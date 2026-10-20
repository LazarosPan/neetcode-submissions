# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Validate a BST using an iterative inorder traversal.

        Invariant: an inorder traversal (left -> node -> right) of a valid
        BST yields keys in strictly increasing order. Strictness also rejects
        duplicates, since the rules require strictly less / strictly greater.

        Approach: simulate the recursion with an explicit stack (no Python
        recursion limit, so a 10,000-node chain is safe). Keep only the value
        of the previously visited node and compare each new node against it.

        Time:  O(n), each node is pushed and popped exactly once.
        Space: O(h) for the stack. h = O(log n) for a balanced tree and
               O(n) for a skewed (chain-like) tree.
        """
        stack = []            # LIFO stack of nodes whose left subtree is being explored
        prev = float("-inf")  # value of the last visited node; -inf is safe
                              # because node values are >= -10^9
        curr = root           # pointer to the node we are descending from

        while curr or stack:
            # 1) Go as far left as possible, remembering the path on the stack.
            while curr:
                stack.append(curr)
                curr = curr.left

            # 2) Left is exhausted: pop the next node in inorder sequence.
            curr = stack.pop()

            # 3) Visit the node: it must be strictly greater than the previous one.
            if curr.val <= prev:
                return False
            prev = curr.val

            # 4) Now explore its right subtree.
            curr = curr.right

        # No ordering violation was found, so the tree is a valid BST.
        return True