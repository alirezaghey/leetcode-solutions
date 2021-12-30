package leetcode

// Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

// Time complexity: O(n) where n is the length of the linked list
// Space complexity: O(1)
func middleNode(head *ListNode) *ListNode {
	fast, slow := head, head

	for fast.Next != nil && fast.Next.Next != nil {
		fast = fast.Next.Next
		slow = slow.Next
	}

	if fast.Next != nil {
		return slow.Next
	} else {
		return slow
	}
}
