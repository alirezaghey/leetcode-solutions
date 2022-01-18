package leetcode

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// Time complexity: O(max(n, m)) where n and m are the number of nodes in tree1 and tree2
// Space complexity: O(max(n, m))
// BFS
// Note: Since wee are misusing slices for queues, the time complexity could potentially
// deteriorate into a quadratic one due to array shifting
func mergeTrees(root1 *TreeNode, root2 *TreeNode) *TreeNode {
	if root2 == nil {
		return root1
	}
	if root1 == nil {
		return root2
	}

	queue := [][]*TreeNode{{root1, root2}}

	for len(queue) > 0 {
		node1, node2 := queue[0][0], queue[0][1]
		queue = queue[1:]

		node1.Val += node2.Val
		if node1.Left == nil {
			node1.Left = node2.Left
		} else if node1.Left != nil && node2.Left != nil {
			queue = append(queue, []*TreeNode{node1.Left, node2.Left})
		}
		if node1.Right == nil {
			node1.Right = node2.Right
		} else if node1.Right != nil && node2.Right != nil {
			queue = append(queue, []*TreeNode{node1.Right, node2.Right})
		}
	}
	return root1
}

// Time complexity: O(max(n, m)) where n and m are the number of nodes in tree1 and tree2
// Space complexity: O(max(n, m))
// DFS approach
func mergeTrees2(root1 *TreeNode, root2 *TreeNode) *TreeNode {
	return dfs(root1, root2)
}

func dfs(node1, node2 *TreeNode) *TreeNode {
	if node1 == nil {
		return node2
	}
	if node2 == nil {
		return node1
	}

	node1.Val += node2.Val
	node1.Left = dfs(node1.Left, node2.Left)
	node1.Right = dfs(node1.Right, node2.Right)

	return node1
}
