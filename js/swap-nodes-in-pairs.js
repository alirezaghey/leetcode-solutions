// https://leetcode.com/problems/swap-nodes-in-pairs/
// Related Topics: Linked List
// Difficulty: Medium

/*
Initial thoughts:
We swap each pair by keeping the second node in a temporary variable
in order to be able to set its next to the initially first node.
Now we set the next property the new second node (which was previously at the first place),
to two nodes ahead, because that is the node that will become the first among the next pair.
The new head of our Linked List will be the initially second node in the list.


Time complexity: O(n) where n is the number of nodes in the Linked List
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
const swapPairs = head => {
  if (head === null || head.next === null) return head;

  let prev = head;
  let curr = head.next;
  head = head.next;

  while (true) {
    const newPrev = curr.next;

    curr.next = prev;
    if (newPrev === null || newPrev.next === null) {
      prev.next = newPrev;
      break;
    }

    prev.next = newPrev.next;

    prev = newPrev;
    curr = prev.next;
  }
  return head;
};
