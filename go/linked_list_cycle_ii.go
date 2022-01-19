package leetcode

// Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

// Time complexity: O(n) where n is the length of the linked list
// Space complexith: O(1)
// Floyd's Hare and Turtoise algorithm
func detectCycle(head *ListNode) *ListNode {
	findMeetingPoint := func(head *ListNode) *ListNode {
		fast, slow := head, head

		for fast.Next != nil && fast.Next.Next != nil {
			fast = fast.Next.Next
			slow = slow.Next
			if fast == slow {
				return fast
			}
		}
		return nil
	}

	if head == nil {
		return head
	}

	meetingPoint := findMeetingPoint(head)
	if meetingPoint == nil {
		return nil
	}

	first, second := head, meetingPoint
	for first != second {
		first, second = first.Next, second.Next
	}
	return first
}
