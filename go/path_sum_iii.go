package leetcode

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func pathSum(root *TreeNode, targetSum int) int {
	dic := make(map[int]int)
	dic[0] = 1
	return dfs(root, 0, targetSum, dic)
}

func dfs(node *TreeNode, prev_sum int, t_sum int, dic map[int]int) int {
	if node == nil {
		return 0
	}

	curr_sum := prev_sum + node.Val
	res := dic[curr_sum-t_sum]
	dic[curr_sum] += 1

	res += dfs(node.Left, curr_sum, t_sum, dic)
	res += dfs(node.Right, curr_sum, t_sum, dic)

	dic[curr_sum] -= 1
	return res
}
