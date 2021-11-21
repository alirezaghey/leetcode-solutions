package leetcode

func buildTree1(inorder []int, postorder []int) *TreeNode {
	postorderIdx := len(inorder) - 1
	return dfs1(0, len(inorder)-1, &postorderIdx, inorder, postorder)
}

func dfs1(left int, right int, postorderIdx *int, inorder []int, postorder []int) *TreeNode {
	if left > right {
		return nil
	}
	if left == right {
		*postorderIdx = (*postorderIdx) - 1
		return &TreeNode{inorder[left], nil, nil}
	}

	rootIdx := findElIdx(left, right, postorder[*postorderIdx], inorder)
	root := TreeNode{inorder[rootIdx], nil, nil}
	*postorderIdx = (*postorderIdx) - 1

	root.Right = dfs1(rootIdx+1, right, postorderIdx, inorder, postorder)
	root.Left = dfs1(left, rootIdx-1, postorderIdx, inorder, postorder)

	return &root

}

func findElIdx(left int, right int, el int, inorder []int) int {
	for i := left; i <= right; i++ {
		if inorder[i] == el {
			return i
		}
	}
	return -1
}

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}
