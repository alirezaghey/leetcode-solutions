package leetcode

// Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

// Time complexity: O(n) where n is the length of the linked list
// Space complexity: O(n)
// recursive approach
func reverseList(head *ListNode) *ListNode {
	return reverse(nil, head)
}

func reverse(prev, curr *ListNode) *ListNode {
	if curr == nil {
		return prev
	}

	head := reverse(curr, curr.Next)
	curr.Next = prev
	return head
}

// Time complexity: O(n) where n is the length of the linked list
// Space complexity: O(1)
// Iterative approach
func reverseList2(head *ListNode) *ListNode {
	var prev *ListNode = nil
	curr := head

	for curr != nil {
		nextNode := curr.Next
		curr.Next = prev
		prev, curr = curr, nextNode
	}
	return prev
}
