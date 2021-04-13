package leetcode

type ListNode struct {
	Val  int
	Next *ListNode
}

func rotateRight(head *ListNode, k int) *ListNode {
	if head == nil {
		return head
	}

	length := listLength(head)
	k = k % length
	if k == 0 {
		return head
	}

	curr := &ListNode{0, head}
	for i := 0; i < k; i++ {
		curr = curr.Next
	}

	end := curr
	curr = &ListNode{0, head}

	for end.Next != nil {
		end, curr = end.Next, curr.Next
	}

	end.Next = head
	newHead := curr.Next
	curr.Next = nil

	return newHead

}

func listLength(node *ListNode) int {
	curr := &ListNode{0, node}
	res := 0

	for curr.Next != nil {
		res += 1
		curr = curr.Next
	}
	return res
}
