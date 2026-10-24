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

        Iterative depth-first search. The `clones` map (original -> copy)
        also serves as the visited set, so each node is copied and pushed
        exactly once, even when the graph contains cycles.

        Args:
            node: Any node of the original graph, or None if the graph is empty.

        Returns:
            The copy of `node`, or None if the graph is empty.

        Complexity:
            Time: O(V + E).
            Space: O(V) auxiliary (map + stack); the O(V + E) copy is the output.
        """
        # Empty graph: nothing to copy.
        if not node:
            return None

        # Copy the starting node first, so there is always something to return.
        root_copy = Node(node.val)

        # Maps each original node to its copy.
        # Doubles as the "visited" set: a node in here has already been copied.
        clones = {node: root_copy}

        # Nodes that are copied but whose neighbor lists are not yet filled in.
        stack = [node]

        while stack:
            # Take the most recently discovered node (last in, first out = DFS).
            current = stack.pop()

            for neighbor in current.neighbors:
                # Not copied yet: copy it now and schedule it for processing.
                # Checking before pushing prevents infinite loops on cycles.
                if neighbor not in clones:
                    clones[neighbor] = Node(neighbor.val)
                    stack.append(neighbor)

                # Runs for every edge, new or not: link copy to copy,
                # never copy to original, so the two graphs share no nodes.
                clones[current].neighbors.append(clones[neighbor])

        # The copy of the starting node; all other copies are reachable from it.
        return root_copy