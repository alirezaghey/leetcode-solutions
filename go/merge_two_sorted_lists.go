package leetcode

// Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

// Time complexity: O(n + m) where n and m are the length of list1 and list2
// Space complexity: O(n + m)
// Recursive approach
func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	return merge(list1, list2, &ListNode{0, nil}).Next
}

func merge(l1, l2, res *ListNode) *ListNode {
	if l1 == nil {
		res.Next = l2
	} else if l2 == nil {
		res.Next = l1
	} else {
		if l1.Val <= l2.Val {
			res.Next = l1
			l1 = l1.Next
		} else {
			res.Next = l2
			l2 = l2.Next
		}
		merge(l1, l2, res.Next)
	}
	return res
}

// Time complexity: O(n + m) where n and m are the length of list1 and list2
// Space complexity: O(1)
// Iterative approach
func mergeTwoLists2(list1 *ListNode, list2 *ListNode) *ListNode {
	dummyHead := &ListNode{0, nil}
	curr := dummyHead

	for list1 != nil && list2 != nil {
		if list1.Val <= list2.Val {
			curr.Next = list1
			list1 = list1.Next
		} else {
			curr.Next = list2
			list2 = list2.Next
		}
		curr = curr.Next
	}

	if list1 != nil {
		curr.Next = list1
	} else if list2 != nil {
		curr.Next = list2
	}
	return dummyHead.Next
}
