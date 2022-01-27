package leetcode

// Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

// Time complexity: O(n)
// Space complexity: O(1)
func deleteDuplicates(head *ListNode) *ListNode {
	dummyHead := &ListNode{0, head}
	prev := dummyHead
	curr := head

	for curr != nil {
		val := curr.Val
		if curr.Next != nil && curr.Next.Val == val {
			curr = curr.Next
			for curr != nil && curr.Val == val {
				curr = curr.Next
			}
		} else {
			prev.Next = curr
			prev, curr = curr, curr.Next
		}
	}
	prev.Next = nil
	return dummyHead.Next
}
