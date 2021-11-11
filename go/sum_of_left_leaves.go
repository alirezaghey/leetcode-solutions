package leetcode

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func sumOfLeftLeaves(root *TreeNode) int {
	return dfs(false, root)
}

func dfs(left bool, node *TreeNode) int {
	if node == nil {
		return 0
	}
	if node.Left == nil && node.Right == nil {
		if left {
			return node.Val
		} else {
			return 0
		}
	}
	return dfs(true, node.Left) + dfs(false, node.Right)
}
