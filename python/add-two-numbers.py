#  https://leetcode.com/problems/add-two-numbers/
#  Related Topics: Linked List, Math
#  Difficulty: Easy


# Initial thoughts:
# Creating a new linked list, we need to loop over the given
# linked lists, adding their values and moving any remaining
# carry to the next digit.
# Keep in mind that some carry may remain after both the linked list
# are completed. We need to add the remaining carry to the result if need be.

# Time complexity: O(Max(n,m)) where n === len(l1) and m === len(l2)
# Space complexity: O(Max(n,m)) where n === len(l1) and m === len(l2)


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        head = ListNode(None)
        curr = head
        carry = 0
        while l1 or l2:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            curr.next = ListNode(carry % 10)
            carry //= 10
            curr = curr.next

        if carry:
            curr.next = ListNode(carry)
        return head.next
