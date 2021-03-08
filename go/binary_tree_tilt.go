package leetcode

import (
	"math"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func findTilt(root *TreeNode) int {
	_, res := dfs(root)
	return res
}

func dfs(node *TreeNode) (int, int) {
	if node == nil {
		return 0, 0
	}

	ls, lt := dfs(node.Left)
	rs, rt := dfs(node.Right)

	return ls + rs + node.Val, lt + rt + int(math.Abs(float64(ls-rs)))
}
