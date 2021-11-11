package leetcode

import (
	"math/rand"
)

type ListNode struct {
	Val  int
	Next *ListNode
}
type Solution struct {
	Data   []int
	Length int
}

func Constructor(head *ListNode) Solution {
	s := Solution{}
	for head != nil {
		s.Data = append(s.Data, head.Val)
		head = head.Next
	}
	s.Length = len(s.Data)
	return s
}

func (this *Solution) GetRandom() int {
	return this.Data[rand.Intn(this.Length)]
}
