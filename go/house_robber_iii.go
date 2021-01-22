package leetcode

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func rob(root *TreeNode) int {
	return dfs(root, false, make(map[Key]int))
}

func dfs(node *TreeNode, taken bool, mem map[Key]int) int {
	if node == nil {
		return 0
	}

	key := Key{node, taken}
	if _, ok := mem[key]; ok {
		return mem[key]
	}

	if taken {
		mem[key] = dfs(node.Left, false, mem) + dfs(node.Right, false, mem)
	} else {
		mem[key] = max(
			dfs(node.Left, true, mem)+dfs(node.Right, true, mem)+node.Val,
			dfs(node.Left, false, mem)+dfs(node.Right, false, mem),
		)
	}
	val, _ := mem[key]
	return val
}

func max(x, y int) int {
	if x > y {
		return x
	} else {
		return y
	}
}

type Key struct {
	node  *TreeNode
	taken bool
}
