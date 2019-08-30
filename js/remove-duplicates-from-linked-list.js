// https://leetcode.com/problems/remove-duplicates-from-sorted-list/
// Related Topics: Linked List
// Difficulty: Easy

/*
Initial thoughts:
Looping over the linked list we are going to compare each node
with its next and if the values are equal, we are going to connect
the current node the the next of the next node.
Note: The condition for our loop is the next of the current node,
otherwise we are going to encounter a null node

Time complexity: O(n) where n === linkedlist.length
Space complexity: O(1) 

*/

/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
const deleteDuplicates = head => {
  if (!head) return head;
  let curr = head;
  while (curr.next) {
    if (curr.val === curr.next.val) curr.next = curr.next.next;
    else curr = curr.next;
  }
  return head;
};
