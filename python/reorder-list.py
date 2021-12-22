from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def find_mid(head):
            fast = slow = head
            while fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
            return slow
        
        def reverse(head):
            first, second = None, head
            while second:
                third = second.next
                second.next = first
                first, second = second, third
            return first
        
        def weave(left, right):
            head = curr = left
            while right:
                curr_next = curr.next
                curr.next = right
                right, left = curr_next, right.next
                curr = curr.next
            return head
        
        if head.next == None: return head
        
        dummy_head = ListNode(0, head)
        mid = find_mid(dummy_head)
        
        left = head
        right = mid.next
        mid.next = None
        
        
        right = reverse(right)
        
        weave(left, right)