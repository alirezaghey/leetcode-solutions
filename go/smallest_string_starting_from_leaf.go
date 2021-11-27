package leetcode

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func smallestFromLeaf(root *TreeNode) string {
	res := "~"
	curr := make([]rune, 0, 20)
	dfs(root, &curr, &res)
	return res
}

func dfs(node *TreeNode, curr *[]rune, res *string) {
	if node == nil {
		return
	}
	if node.Left == nil && node.Right == nil {
		*curr = append(*curr, rune(int('a')+node.Val))
		copy_curr := make([]rune, len(*curr))
		for i := 0; i < len(*curr); i++ {
			copy_curr[len(copy_curr)-1-i] = (*curr)[i]
		}
		str := string(copy_curr)
		if str < *res {
			*res = str
		}
		*curr = (*curr)[:len(*curr)-1]
		return
	}

	*curr = append(*curr, rune(int('a')+node.Val))
	dfs(node.Left, curr, res)
	dfs(node.Right, curr, res)
	*curr = (*curr)[:len(*curr)-1]
}
