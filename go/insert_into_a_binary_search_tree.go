package leetcode

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// iterative solution
// Time complexity: O(log n) for a balanced tree, otherwise O(n)
// Space complexity: O(1)
func insertIntoBST(root *TreeNode, val int) *TreeNode {
	if root == nil {
		node := TreeNode{val, nil, nil}
		return &node
	}

	curr := root
	for true {
		if val < curr.Val {
			if curr.Left == nil {
				node := TreeNode{val, nil, nil}
				curr.Left = &node
				break
			} else {
				curr = curr.Left
			}
		} else {
			if curr.Right == nil {
				node := TreeNode{val, nil, nil}
				curr.Right = &node
				break
			} else {
				curr = curr.Right
			}
		}
	}
	return root
}

// recursive solution
// Time complexity: O(log n) for a balanced tree, otherwise O(n)
// Space complexity: O(log n) for the stack in a balanced tree, otherwise O(n)
func insertIntoBST2(root *TreeNode, val int) *TreeNode {
	return insert(root, val)
}

func insert(node *TreeNode, val int) *TreeNode {
	if node == nil {
		newNode := TreeNode{val, nil, nil}
		return &newNode
	}

	if val < node.Val {
		node.Left = insert(node.Left, val)
	} else {
		node.Right = insert(node.Right, val)
	}
	return node
}
