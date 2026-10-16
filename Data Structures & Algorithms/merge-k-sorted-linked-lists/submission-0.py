# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode] :
        """
        Merge k sorted linked lists into one sorted linked list.

        Approach (divide and conquer):
            Merge the lists in pairs, round by round. Each round halves the
            number of lists, so there are ceil(log2 k) rounds. A leftover
            odd list simply waits for the next round.

        Args:
            lists: k linked lists, each sorted in ascending order.

        Returns:
            The head of the merged sorted list (None if there are no nodes).

        Complexity:
            Time O(N log k), where N is the total number of nodes.
            Space O(1) extra (the lists are relinked, not copied).
        """
        # No lists at all: nothing to merge.
        if not lists:
            return None

        # step = distance between the two lists merged in the current round.
        step = 1
        while step < len(lists):
            # Merge lists[i] with lists[i + step] and store the result in lists[i].
            # If i + step is out of range, that list is the odd one out and waits.
            for i in range(0, len(lists) - step, 2 * step):
                lists[i] = self.mergeTwoLists(lists[i], lists[i + step])
            # Next round: merged lists are twice as far apart.
            step *= 2

        # After the last round, everything is merged into lists[0].
        return lists[0]

    def mergeTwoLists(self, first: Optional[ListNode], second: Optional[ListNode]) -> Optional[ListNode] :
        """
        Merge two sorted linked lists into one sorted linked list.

        Args:
            first: head of the first sorted list (may be None).
            second: head of the second sorted list (may be None).

        Returns:
            The head of the merged sorted list.

        Complexity:
            Time O(len(first) + len(second)), Space O(1).
        """
        # Fake node in front of the merged list, so the head needs no special case.
        node_before_head = ListNode()
        # Last node of the merged list built so far.
        tail = node_before_head

        # Repeatedly attach the smaller of the two current heads.
        while first and second:
            if first.val <= second.val:
                tail.next = first
                first = first.next
            else:
                tail.next = second
                second = second.next
            tail = tail.next

        # One list is empty. The other holds the remaining nodes, which are already
        # sorted and >= everything attached so far, so link them in one step.
        tail.next = first or second

        # node_before_head.next is the real head of the merged list.
        return node_before_head.next