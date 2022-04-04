from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Initial thoughts:
    We move a first pointer k positions forward and save a reference to the node.
    Then we create another pointer at head and move it forward in sync with the first pointer while the first pointer hasn't hit the end of the linked list. When the first pointer hits the end, the second pointer is at the second node that needs to be swapped. Then we swap.

    Time complexity: O(n)
    Space complexity: O(1)
    """

    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        first = dummy_head = ListNode(0, head)

        for _ in range(k):
            first = first.next

        left_node = first
        second = dummy_head
        while first:
            first, second = first.next, second.next

        left_node.val, second.val = second.val, left_node.val

        return head
