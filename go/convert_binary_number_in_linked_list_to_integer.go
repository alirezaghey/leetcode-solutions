package leetcode

type ListNode struct {
	Val  int
	Next *ListNode
}

func getDecimalValue(head *ListNode) int {
	res, curr := 0, head
	for curr != nil {
		res <<= 1
		res |= curr.Val
		curr = curr.Next
	}
	return res
}
