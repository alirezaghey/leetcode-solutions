package leetcode

func maximalPathQuality(values []int, edges [][]int, maxTime int) int {
	adj_list := make([][]Node, len(values))
	for i := 0; i < len(adj_list); i++ {
		adj_list[i] = make([]Node, 0)
	}

	for _, node := range edges {
		u, v, t := node[0], node[1], node[2]
		adj_list[u] = append(adj_list[u], Node{v, t})
		adj_list[v] = append(adj_list[v], Node{u, t})
	}

	res := Res{values[0]}
	visited := make(map[int]bool)
	visited[0] = true
	backtrack(0, 0, values[0], maxTime, adj_list, visited, values, &res)
	return res.res

}

type Res struct {
	res int
}
type Node struct {
	nei  int
	time int
}

func backtrack(curr_node int, curr_time int, curr_val int, max_time int, adj_list [][]Node, visited map[int]bool, values []int, res *Res) {
	if curr_time <= max_time/2 && res.res < curr_val {
		res.res = curr_val
	}
	if curr_node == 0 && res.res < curr_val {
		res.res = curr_val
	}

	for _, node := range adj_list[curr_node] {
		nei, t := node.nei, node.time

		if curr_time+t <= max_time {
			if _, ok := visited[nei]; ok == false {
				visited[nei] = true
				backtrack(nei, curr_time+t, curr_val+values[nei], max_time, adj_list, visited, values, res)
				delete(visited, nei)
			} else {
				backtrack(nei, curr_time+t, curr_val, max_time, adj_list, visited, values, res)
			}
		}

	}

}
