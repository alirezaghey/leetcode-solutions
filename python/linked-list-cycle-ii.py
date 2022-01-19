from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # Time complexity: O(n) where n is the length of the linked list
    # Space complexity: O(1)
    # Floyd's Hare and Turtoise algorithm
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def find_meeting_point(head):
            fast = slow = head
            while fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
                if fast == slow:
                    return fast
            return None
        
        if not head: return head
        meeting_point = find_meeting_point(head)
        if meeting_point == None:
            return None
        
        first, second = head, meeting_point
        
        while first != second:
            first, second = first.next, second.next
        return first