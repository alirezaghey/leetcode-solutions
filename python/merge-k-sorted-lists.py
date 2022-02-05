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

from typing import List, Optional
from queue import PriorityQueue
from collections import heapq
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists3(self, lists: List[ListNode]) -> ListNode:
        # Save a pointer to the current beginning of each linked list
        currPointers = []
        for i in range(len(lists)):
            currPointers.append(lists[i])

        head = ListNode(0)
        curr = head
        while True:
            done = True
            currMin = 2 ** 31 - 1
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

# Optimization:
# Using a priority queue we can reduce the comparison and lookup time
# of the smallest value from k to log k.
# The algorithm is almost like the one used in the previous example.

# Time Complexity: O(n * log k) where n == the number of all the nodes in all the linked lists and k == the number of the linked lists
# Sapce Complexity: O(k) where k == the number of linked lists since we need to load the current of each linked list in the priority queue
    def mergeKLists2(self, lists: List[ListNode]) -> ListNode:
        # Load the first node from every linked list into a priority queue
        prQueue = PriorityQueue()
        for node in lists:
            if node:
                print(node.val)
                prQueue.put((node.val, node))

        head = ListNode(0)
        curr = head
        while not prQueue.empty():
            val, node = prQueue.get()
            curr.next = node
            curr = curr.next
            if node.next:
                prQueue.put((node.next.val, node.next))

        return head.next


    # Time complexity: O(n * log k) where n is the number of nodes in all lists
    # and k is the number of lists
    # Space complexity: O(k)
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        hp = [(node.val, i, node) for i, node in enumerate(lists) if node]
        heapq.heapify(hp)
        counter = len(lists)
        dummy_head = curr = ListNode()
        while hp:
            _, _, node = heapq.heappop(hp)
            curr.next = node
            if node.next:
                heapq.heappush(hp, (node.next.val, counter, node.next))
                counter += 1
            curr = curr.next
        return dummy_head.next