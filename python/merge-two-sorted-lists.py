from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Time complexity: O(n + m) where n and m are the length of list1 and list2
    # Space complexity: O(n + m)
    # recursive approach
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def merge(l1, l2, res):
            if not l1:
                res.next = l2
            elif not l2:
                res.next = l1
            else:
                if l1.val <= l2.val:
                    res.next = l1
                    l1 = l1.next
                else:
                    res.next = l2
                    l2 = l2.next
                merge(l1, l2, res.next)
            return res
        return merge(list1, list2, ListNode()).next
                
    # Time complexity: O(n + m) where n and m are the length of list1 and list2
    # Space complexity: O(1)
    # Iterative approach
    def mergeTwoLists2(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = curr = ListNode()
        
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        
        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2
        
        return dummy_head.next
        