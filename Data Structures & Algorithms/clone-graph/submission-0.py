"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        q&a
        Are all nodes connected? Yes. For a nonempty graph, every node is reachable from the input node.
        Do we know if there are circles in the graph? They may exist.
        Even your first example allows traversal from node 1 to node 2 and back, so your approach must handle revisiting nodes.
        What is the number of nodes in the graph? 0 <= The number of nodes in the graph <= 100.
        What is the range of values that exist in the nodes? 1 <= Node.val <= 100
        Can I have some examples?
        
        DFS approach
        initialize an node_copy variable as a new Node()
        initialize an empty stack []
        initialize a defaultdict to store the original and the copy

        TC = O(V+E), SC = O(V+E)
        """
        if not node:
            return None

        node_copy = Node(node.val)
        clones = {node: node_copy}
        stack = [node]

        while stack:
            curr = stack.pop()
            
            for neighbor in curr.neighbors:
                if neighbor not in clones:
                    clones[neighbor] = Node(neighbor.val)
                    stack.append(neighbor)

                clones[curr].neighbors.append(clones[neighbor])	
                
        return node_copy