package leetcode

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func deleteNode(root *TreeNode, key int) *TreeNode {
	if root == nil {
		return nil
	}

	if root.Val < key {
		root.Right = deleteNode(root.Right, key)
	} else if root.Val > key {
		root.Left = deleteNode(root.Left, key)
	} else {
		if root.Left == nil && root.Right == nil { // has no children
			return nil
		} else if root.Left == nil && root.Right != nil { // has only right child
			return root.Right
		} else if root.Right == nil && root.Left != nil { // has only left child
			return root.Left
		} else { // has both left and right children
			curr := root.Right
			for curr.Left != nil {
				curr = curr.Left
			}
			root.Val = curr.Val
			root.Right = deleteNode(root.Right, curr.Val)
		}
	}
	return root
}
