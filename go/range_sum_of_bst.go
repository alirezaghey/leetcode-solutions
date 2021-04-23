package leetcode

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func rangeSumBST(root *TreeNode, low int, high int) int {
	return dfs(root, low, high)
}

func dfs(node *TreeNode, low, high int) int {
	if node == nil {
		return 0
	}

	res := 0
	if node.Val >= low && node.Val <= high {
		res += node.Val
	}

	if node.Val > low {
		res += dfs(node.Left, low, high)
	}
	if node.Val < high {
		res += dfs(node.Right, low, high)
	}

	return res
}
