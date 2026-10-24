"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """Returns a deep copy of a connected undirected graph.

        Uses an iterative depth-first search. A hash map from each original
        node to its clone doubles as the "visited" set, so every node is
        cloned and pushed onto the stack exactly once, even when cycles exist.

        Args:
            node: Any node of the original graph (the one with val 1 in the
                problem statement), or None for an empty graph.

        Returns:
            The clone of the input node, or None if the graph is empty.

        Complexity:
            Time: O(V + E), each node is expanded once and each edge is
                traversed twice (once per direction).
            Space: O(V) auxiliary (hash map + stack); the cloned graph itself
                occupies O(V + E) and is the output.
        """
        if not node:
            return None

        original_to_clone = {node: Node(node.val)}
        nodes_to_expand = [node]

        while nodes_to_expand:
            current_original = nodes_to_expand.pop()

            for neighbor_original in current_original.neighbors:
                # First discovery: create the clone and schedule its expansion.
                if neighbor_original not in original_to_clone:
                    original_to_clone[neighbor_original] = Node(neighbor_original.val)
                    nodes_to_expand.append(neighbor_original)

                # Wire the edge between clones (not between originals).
                original_to_clone[current_original].neighbors.append(
                    original_to_clone[neighbor_original]
                )

        return original_to_clone[node]