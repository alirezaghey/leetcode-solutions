from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Time complexity: O(n) where n is the length of the linked list
    # Space complexity: O(1)
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
        if fast.next:
            return slow.next
        else:
            return slow