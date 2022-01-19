package leetcode

// Definition for a Node.
type Node struct {
	Val   int
	Left  *Node
	Right *Node
	Next  *Node
}

// Time complexity: O(n) where n is the number of nodes
// Space complexity: O(n)
// DFS
func connect(root *Node) *Node {
	if root == nil {
		return root
	}
	if root.Left != nil {
		root.Left.Next = root.Right
		if root.Next != nil {
			root.Right.Next = root.Next.Left
		}
	}

	connect(root.Left)
	connect(root.Right)
	return root
}

// Time complexity: O(n) where n is the number of nodes
// Space complexity: O(1)
// BFS
// Note: This is an optimized version for space
func connect2(root *Node) *Node {
	head := root

	for head != nil {
		curr := head
		for curr != nil {
			if curr.Left != nil {
				curr.Left.Next = curr.Right
				if curr.Next != nil {
					curr.Right.Next = curr.Next.Left
				}
			}
			curr = curr.Next
		}
		head = head.Left
	}
	return root
}

// Time complexity: O(n) where n is the number of nodes
// Space complexity: O(n)
// BFS
func connect3(root *Node) *Node {
	if root == nil {
		return root
	}

	deq := []*Node{root}

	for len(deq) > 0 {
		n := len(deq)
		for i := 0; i < n; i++ {
			node := deq[0]
			deq = deq[1:]
			if i < n-1 {
				node.Next = deq[0]
			}
			if node.Left != nil {
				deq = append(deq, node.Left)
			}
			if node.Right != nil {
				deq = append(deq, node.Right)
			}
		}
	}
	return root
}
