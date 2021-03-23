from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i = 1
        odd_dummy_head = odd_curr = ListNode(0)
        even_dummy_head = even_curr = ListNode(0)
        curr = head
        
        while curr:
            if i % 2 == 0:
                even_curr.next = curr
                even_curr = even_curr.next
            else:
                odd_curr.next = curr
                odd_curr = odd_curr.next
            curr = curr.next
            i += 1
        
        odd_curr.next = even_dummy_head.next
        even_curr.next = None
        
        return odd_dummy_head.next