# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Remove the n-th node from the end of a singly linked list in one pass.

        Approach (two pointers with a fixed gap):
            Move `leading_node` n steps ahead of `node_before_target`.
            Then advance both together until `leading_node` is on the last node.
            Because the gap stays n, `node_before_target` ends up one step
            before the target (the n-th node from the end).

        Args:
            head: First node of the list (1 <= length <= 30).
            n: Position from the END of the list, 1-indexed
               (n=1 is the last node, n=length is the head).

        Returns:
            The head of the updated list (None if the list becomes empty).

        Complexity:
            Time O(length), Space O(1).
        """
        # node_before_headead. It lets us delete the head itself
        # (e.g. [1,2] with n=2) without a special case.
        node_before_head = ListNode(0, head)

        node_before_target = node_before_head
        leading_node = node_before_head

        # Advance leading_node n steps to create a gap of n nodes.
        for _ in range(n):
            leading_node = leading_node.next

        # Move both pointers together until leading_node is the last node.
        # The gap stays n, so node_before_target ends up right before the target.
        while leading_node.next:
            leading_node = leading_node.next
            node_before_target = node_before_target.next

        # Delete the target by bypassing it.
        node_before_target.next = node_before_target.next.next

        # node_before_head.next is the real head (it changes only if the head was deleted).
        return node_before_head.next