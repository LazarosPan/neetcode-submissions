"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    # Constraint from the problem: 1 <= Node.val <= 100, and values are unique.
    MAX_NODE_VALUE = 100

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """Returns a deep copy of a connected undirected graph.

        Same traversal as the hash-map version, but exploits the constraint that
        node values are unique integers in [1, 100]. The value itself is the
        array index, which gives O(1) worst-case lookup with no hashing.

        Args:
            node: Any node of the original graph, or None for an empty graph.

        Returns:
            The clone of the input node, or None if the graph is empty.

        Complexity:
            Time: O(V + E).
            Space: O(V) auxiliary (fixed-size array + stack); the cloned graph
                occupies O(V + E) and is the output.

        Note:
            Valid only while node values are unique and bounded. Otherwise,
            key a hash map by node identity instead (Solution 1).
        """
        if not node:
            return None

        clone_by_value = [None] * (self.MAX_NODE_VALUE + 1)  # index 0 unused
        clone_by_value[node.val] = Node(node.val)
        nodes_to_expand = [node]

        while nodes_to_expand:
            current_original = nodes_to_expand.pop()

            for neighbor_original in current_original.neighbors:
                # First discovery: create the clone and schedule its expansion.
                if clone_by_value[neighbor_original.val] is None:
                    clone_by_value[neighbor_original.val] = Node(neighbor_original.val)
                    nodes_to_expand.append(neighbor_original)

                # Wire the edge between clones (not between originals).
                clone_by_value[current_original.val].neighbors.append(
                    clone_by_value[neighbor_original.val]
                )

        return clone_by_value[node.val]