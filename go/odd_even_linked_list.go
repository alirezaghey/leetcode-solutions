package leetcode

type ListNode struct {
	Val  int
	Next *ListNode
}

func oddEvenList(head *ListNode) *ListNode {
	even_dummy_head := &ListNode{0, nil}
	even_curr := even_dummy_head
	odd_dummy_head := &ListNode{0, nil}
	odd_curr := odd_dummy_head
	curr := head
	i := 1

	for curr != nil {
		if i%2 == 0 {
			even_curr.Next = curr
			even_curr = even_curr.Next
		} else {
			odd_curr.Next = curr
			odd_curr = odd_curr.Next
		}
		curr = curr.Next
		i++
	}

	odd_curr.Next = even_dummy_head.Next
	even_curr.Next = nil
	return odd_dummy_head.Next
}
