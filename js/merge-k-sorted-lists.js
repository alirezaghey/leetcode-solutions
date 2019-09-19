// https://leetcode.com/problems/merge-k-sorted-lists/
// Related Topics: Linked List, Divide and Conquer, Heap
// Difficulty: Hard

/*
Initial thoughts:
We are going to loop over every linked lists and check which of them
has the smallest value and weave our way forward until we have reached
the end of every one of the linked lists.

Time complexity: O(k * n) where k === the number of linked lists and n is the number of all the nodes in all the linked lists
Space complexity: O(k) where k === the number of linked lists because we are going to hold a pointer to the beginning of each
linked list in it and advance it if we merge that particular node. 
*/

/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode[]} lists
 * @return {ListNode}
 */
const mergeKLists = lists => {
  // Create an array with pointers to the beginning of each list
  const currPointers = [];
  for (let i = 0; i < lists.length; i++) {
    currPointers.push(lists[i]);
  }

  const head = new ListNode();
  let curr = head;
  while (true) {
    let min = Number.MAX_SAFE_INTEGER;
    let indexMin = -1;
    let done = true;
    for (let i = 0; i < currPointers.length; i++) {
      if (currPointers[i] && currPointers[i].val < min) {
        done = false;
        min = currPointers[i].val;
        indexMin = i;
      }
    }
    if (done) break;
    curr.next = currPointers[indexMin];
    curr = curr.next;
    currPointers[indexMin] = currPointers[indexMin].next;
  }
  return head.next;
};
