# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Find the maximum depth of a binary tree using iterative DFS.

        The depth is the number of nodes along the longest path
        from the root to the farthest leaf node.

        Args:
            root: The root node of the binary tree.

        Returns:
            int: The maximum depth of the tree.
                 Returns 0 if the tree is empty.

        Approach:
            Iterative Depth-First Search (DFS) using a stack.

            1. Initialize a stack containing (root, depth=1).
            2. Pop a node and its depth from the stack.
            3. Update max_depth if the current depth is greater.
            4. Push existing children with depth + 1.
            5. Repeat until the stack is empty.

            Each stack entry stores (node, depth), allowing us
            to track depth independently of the traversal order.

        Complexity:
            Time: O(n)
                Each node is visited exactly once.

            Space: O(h)
                The stack holds at most O(h) nodes,
                where h is the height of the tree.

                Balanced tree: O(log n)
                Skewed tree:   O(n)
        """

        # Edge case: An empty tree has depth 0.
        if not root:
            return 0

        # Store (node, depth) pairs to track each node's depth.
        # The root starts at depth 1.
        stack = [(root, 1)]

        # Track the maximum depth encountered during traversal.
        max_depth = 0

        # Continue exploring until there are no nodes left.
        while stack:

            # Pop the most recently added node (LIFO -> DFS).
            node, depth = stack.pop()

            # Update the maximum depth if necessary.
            max_depth = max(max_depth, depth)

            # Push the left child with its corresponding depth.
            # Only push existing children to avoid None entries.
            if node.left:
                stack.append((node.left, depth + 1))

            # Push the right child with its corresponding depth.
            if node.right:
                stack.append((node.right, depth + 1))

        # Return the deepest level encountered.
        return max_depth