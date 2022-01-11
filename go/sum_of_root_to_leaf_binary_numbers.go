package leetcode

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func sumRootToLeaf(root *TreeNode) int {
	return dfs(root, 0)
}

func dfs(node *TreeNode, curr int) int {
	if node == nil {
		return 0
	}

	curr <<= 1
	curr |= node.Val

	if node.Left == nil && node.Right == nil {
		return curr
	}
	return dfs(node.Left, curr) + dfs(node.Right, curr)
}
