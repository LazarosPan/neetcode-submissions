# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Node currently being processed.
        # Initially, this is the first node.
        current = head

        # First node of the already-reversed section.
        # Initially, nothing has been reversed.
        previous = None

        while current:
            # Save the next node BEFORE changing current.next.
            # Otherwise, we would lose the unreversed remainder.
            next_node = current.next

            # Reverse current's arrow.
            # It now points to the previous node.
            current.next = previous

            # The current node is now the first node
            # of the reversed section.
            previous = current

            # Move forward to the node saved earlier.
            current = next_node

        # current is now None.
        # previous points to the new first node.
        return previous