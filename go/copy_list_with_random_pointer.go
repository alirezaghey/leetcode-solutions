package leetcode

// Definition for a Node.
type Node struct {
	Val    int
	Next   *Node
	Random *Node
}

// Time complexity: O(n) where n is the length of the linked list
// Space complexity: O(n)
func copyRandomList(head *Node) *Node {
	dic := make(map[*Node]*Node)

	dummy_head := &Node{0, nil, nil}
	curr := dummy_head

	curr_old := head

	for curr_old != nil {
		curr.Next = &Node{curr_old.Val, nil, nil}
		dic[curr_old] = curr.Next

		curr_old, curr = curr_old.Next, curr.Next
	}

	curr_old = head
	for curr_old != nil {
		if curr_old.Random != nil {
			dic[curr_old].Random = dic[curr_old.Random]
		}
		curr_old = curr_old.Next
	}

	return dummy_head.Next
}
