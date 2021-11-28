package leetcode

func allPathsSourceTarget(graph [][]int) [][]int {
	res := make([][]int, 0, 10)
	dfs(graph, 0, []int{0}, &res)
	return res
}

func dfs(graph [][]int, node int, partialRes []int, res *[][]int) {
	if node == len(graph)-1 {
		cpPartialRes := make([]int, len(partialRes))
		copy(cpPartialRes, partialRes)
		*res = append(*res, cpPartialRes)
		return
	}

	for _, nei := range graph[node] {
		partialRes = append(partialRes, nei)
		dfs(graph, nei, partialRes, res)
		partialRes = partialRes[:len(partialRes)-1]
	}
}
