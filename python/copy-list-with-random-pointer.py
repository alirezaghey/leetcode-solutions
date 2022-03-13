from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    # Time complexity: O(n) where n is the length of the linked list
    # Space complexity: O(n)
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        dummy_head = curr = Node(0)
        dic = {}
        
        curr_original = head
        
        while curr_original:
            curr.next = Node(curr_original.val)
            curr = curr.next
            dic[curr_original] = curr
            curr_original = curr_original.next
        
        curr_original = head
        while curr_original:
            if curr_original.random:
                dic[curr_original].random = dic[curr_original.random]
            curr_original = curr_original.next
        
        return dummy_head.next