#  https://leetcode.com/problems/merge-k-sorted-lists/
#  Related Topics: Linked List, Divide and Conquer, Heap
#  Difficulty: Hard


# Initial thoughts:
# We are going to loop over every linked lists and check which of them
# has the smallest value and weave our way forward until we have reached
# the end of every one of the linked lists.

# Time complexity: O(k * n) where k === the number of linked lists and n is the number of all the nodes in all the linked lists
# Space complexity: O(k) where k === the number of linked lists because we are going to hold a pointer to the beginning of each
# linked list in it and advance it if we merge that particular node.

from typing import List
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKSortedLists(self, l: List[ListNode]) -> ListNode:
        # Save a pointer to the current beginning of each linked list
        currPointers = []
        for i in range(len(l)):
            currPointers.append(l[i])

        head = ListNode(0)
        curr = head
        while True:
            done = True
            currMin = 2 ** 21 - 1
            currMinIndex = -1
            for i in range(len(currPointers)):
                if currPointers[i] != None and currPointers[i].val < currMin:
                    done = False
                    currMin = currPointers[i].val
                    currMinIndex = i
            if done:
                break
            curr.next = currPointers[currMinIndex]
            curr = curr.next
            currPointers[currMinIndex] = currPointers[currMinIndex].next

        return head.next
