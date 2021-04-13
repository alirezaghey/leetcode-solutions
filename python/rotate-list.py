class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return head
        
        def list_length(node):
            dummy_head = ListNode(0, node)
            res = 0
            while dummy_head.next:
                res += 1
                dummy_head = dummy_head.next
            return res
        
        length = list_length(head)
        k = k % length
        if k == 0: return head
        
        curr = ListNode(0, head)
        for _ in range(k):
            curr = curr.next
        
        end = curr
        curr = ListNode(0, head)
        
        while end.next:
            end, curr = end.next, curr.next
        
        end.next = head
        new_head = curr.next
        curr.next = None
        
        return new_head