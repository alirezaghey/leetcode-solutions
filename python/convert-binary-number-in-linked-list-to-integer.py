class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        res, curr = 0, head
        while curr:
            res <<= 1
            res |= curr.val
            curr = curr.next
        return res