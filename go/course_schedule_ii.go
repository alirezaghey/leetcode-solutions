package leetcode

func findOrder(numCourses int, prerequisites [][]int) []int {
	indegree := make([]int, numCourses)
	adj_list := make(map[int][]int)

	for _, el := range prerequisites {
		course, pre := el[0], el[1]

		indegree[course] += 1
		if _, ok := adj_list[course]; ok == false {
			adj_list[course] = make([]int, 0, 1)
		}

		adj_list[pre] = append(adj_list[pre], course)
	}

	stack := make([]int, 0)
	res := make([]int, 0)

	for i, el := range indegree {
		if el == 0 {
			stack = append(stack, i)
		}
	}

	for len(stack) > 0 {
		node := stack[len(stack)-1]
		stack = stack[:len(stack)-1]

		for _, el := range adj_list[node] {
			indegree[el] -= 1
			if indegree[el] == 0 {
				stack = append(stack, el)
			}
		}

		res = append(res, node)
	}

	if len(res) == numCourses {
		return res
	} else {
		return make([]int, 0)
	}
}
