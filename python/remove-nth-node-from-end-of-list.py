# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Related Topics: Linked List, Two Pointers
# Difficulty: Medium


# Initial thoughts:
# Using a two pointer approach, we are going to advance a forerunner n times
# Then we are going to advance the forerunner and another pointer that starts
# from head until forerunner.next hits None.
# Now our second pointer is one element behing the node we want to remove.
# In this algorithm we are told that n is always valid.
# If n equals the length of the linked list, the forerunner will already be
# at the end of the linked list after the first loop and we can't enter the second loop.
# That is because the nth node that needs to be removed is the first node in this case,
# so we can just return head.next.

# Time complexity: O(n) where n is the number of nodes in the list
# Space complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        vanguard = head
        for i in range(n):
            vanguard = vanguard.next

        if vanguard == None:  # if vanguard is None the nth element is the head itslef
            return head.next

        prev = head
        while vanguard.next != None:
            vanguard = vanguard.next
            prev = prev.next

        prev.next = prev.next.next

        return head
