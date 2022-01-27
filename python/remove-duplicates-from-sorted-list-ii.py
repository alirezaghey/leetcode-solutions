from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = prev = ListNode(0, head)
        curr = head

        while curr:
            val = curr.val
            if curr.next and curr.next.val == val:
                curr = curr.next
                while curr and curr.val == val:
                    curr = curr.next
            else:
                prev.next = curr
                prev, curr = curr, curr.next
        prev.next = None
        return dummy_head.next
