from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    # Recursive approach
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(prev_node, curr_node):
            if curr_node == None:
                return prev_node
            
            head = reverse(curr_node, curr_node.next)
            curr_node.next = prev_node
            return head
        return reverse(None, head)
            
    
    # Time complexity: O(n)
    # Space complexity: O(1)
    # Iterative approach
    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        
        while curr:
            next_node = curr.next
            curr.next = prev
            prev, curr = curr, next_node
        return prev