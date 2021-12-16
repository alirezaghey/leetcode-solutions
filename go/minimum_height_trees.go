package leetcode

func findMinHeightTrees(n int, edges [][]int) []int {
	if n < 3 {
		res := make([]int, n)
		for i := 0; i < n; i++ {
			res[i] = i
		}
		return res
	}

	adj_list := make(map[int]Neighbor)

	for _, el := range edges {
		x, y := el[0], el[1]

		if _, ok := adj_list[x]; !ok {
			adj_list[x] = Neighbor{make(map[int]bool)}
		}
		if _, ok := adj_list[y]; !ok {
			adj_list[y] = Neighbor{make(map[int]bool)}
		}

		xNeighbors := adj_list[x]
		yNeighbors := adj_list[y]

		xNeighbors.neighbors[y] = true
		yNeighbors.neighbors[x] = true
	}

	leafs := make([]int, 0, 100)
	for key, value := range adj_list {
		if len(value.neighbors) == 1 {
			leafs = append(leafs, key)
		}
	}

	for len(adj_list) > 2 {
		new_leafs := make([]int, 0)
		for _, leaf := range leafs {
			for neighbor := range adj_list[leaf].neighbors {
				delete(adj_list[neighbor].neighbors, leaf)
				if len(adj_list[neighbor].neighbors) == 1 {
					new_leafs = append(new_leafs, neighbor)
				}
			}
			delete(adj_list, leaf)
		}
		leafs = new_leafs
	}
	res := make([]int, 0)
	for key := range adj_list {
		res = append(res, key)
	}
	return res
}

type Neighbor struct {
	neighbors map[int]bool
}
