package leetcode

type ListNode struct {
	Val  int
	Next *ListNode
}

func insertionSortList(head *ListNode) *ListNode {
	dummy := &ListNode{0, nil}
	p := dummy
	dummy.Next = head
	curr := head

	for curr != nil && curr.Next != nil {
		val := curr.Next.Val
		if curr.Val < val {
			curr = curr.Next
			continue
		}
		if p.Next.Val > val {
			p = dummy
		}
		for p.Next.Val < val {
			p = p.Next
		}
		new := curr.Next
		curr.Next = new.Next
		new.Next = p.Next
		p.Next = new
	}
	return dummy.Next
}
