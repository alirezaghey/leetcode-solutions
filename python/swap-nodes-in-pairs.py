#  https://leetcode.com/problems/swap-nodes-in-pairs/
#  Related Topics: Linked List
#  Difficulty: Medium


# Initial thoughts:
# We swap each pair by keeping the second node in a temporary variable
# in order to be able to set its next to the initially first node.
# Now we set the next property the new second node (which was previously at the first place),
# to two nodes ahead, because that is the node that will become the first among the next pair.
# The new head of our Linked List will be the initially second node in the list.


# Time complexity: O(n) where n is the number of nodes in the Linked List
# Space complexity: O(1)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head

        prev = head
        curr = head.next
        head = head.next

        while True:
            newPrev = curr.next

            curr.next = prev
            if newPrev == None or newPrev.next == None:
                prev.next = newPrev
                break

            prev.next = newPrev.next

            prev = newPrev
            curr = prev.next

        return head
