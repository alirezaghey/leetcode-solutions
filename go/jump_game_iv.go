package leetcode

// BFS approach
// Time complexity: O(V) where V is the length of the array. The indices are considered the nodes of the graph
// Space complexity: O(V)
// Note: If we don't properly optimize it the complexity becomes O(V + E) where E could be V^2
// in the worst case where all the elements in the array except for the first and last
// are the same. It creates a graph where each node is connecte directly to every other one
func minJumps(arr []int) int {
	if len(arr) == 1 {
		return 0
	}

	N := len(arr)
	adjList := make(map[int][]int)
	for i, el := range arr {
		if _, ok := adjList[el]; ok == false {
			adjList[el] = make([]int, 0, 10)
		}
		adjList[el] = append(adjList[el], i)
	}

	deq := []int{0}
	seen := make(map[int]bool)
	seen[0] = true
	res := 0

	for len(deq) > 0 {
		res += 1
		newDeq := make([]int, 0, 10)

		for _, node := range deq {
			if _, ok := seen[node+1]; node < N-1 && ok == false {
				if node+1 == N-1 {
					return res
				}
				newDeq = append(newDeq, node+1)
				seen[node+1] = true
			}
			if _, ok := seen[node-1]; node > 0 && ok == false {
				newDeq = append(newDeq, node-1)
				seen[node-1] = true
			}

			for _, nei := range adjList[arr[node]] {
				if nei == N-1 {
					return res
				}
				if _, ok := seen[nei]; ok == false {
					newDeq = append(newDeq, nei)
					seen[nei] = true
				}
			}
			adjList[arr[node]] = nil
		}
		deq = newDeq
	}
	return -1
}
