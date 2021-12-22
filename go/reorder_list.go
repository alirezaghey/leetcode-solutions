package leetcode

type ListNode struct {
	Val  int
	Next *ListNode
}

func reorderList(head *ListNode) {
	if head.Next == nil {
		return
	}

	dummyHead := ListNode{0, head}
	mid := findMid(&dummyHead)

	left := head
	right := mid.Next
	mid.Next = nil

	right = reverse(right)

	weave(left, right)
}

func findMid(head *ListNode) *ListNode {
	fast := head
	slow := head

	for fast.Next != nil && fast.Next.Next != nil {
		fast = fast.Next.Next
		slow = slow.Next
	}
	return slow
}

func reverse(head *ListNode) *ListNode {
	var first *ListNode = nil
	second := head

	for second != nil {
		third := second.Next
		second.Next = first
		first, second = second, third
	}
	return first
}

func weave(left, right *ListNode) {
	curr := left

	for right != nil {
		curr_next := curr.Next
		curr.Next = right
		left, right = right.Next, curr_next
		curr = curr.Next
	}
}
