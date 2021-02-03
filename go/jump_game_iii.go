package leetcode

// TC: O(n)
// SC: O(n)
// optimized to not use auxiliary state to track visited nodes
func canReach(arr []int, start int) bool {
	if arr[start] == 0 {
		return true
	}

	N := len(arr)
	stack := make([][]int, 0)
	stack = append(stack, []int{start, arr[start]})
	arr[start] = -1

	for len(stack) > 0 {
		node := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		i, d := node[0], node[1]

		forward, backward := i+d, i-d
		if forward < N && arr[forward] != -1 {
			if arr[forward] == 0 {
				return true
			}
			stack = append(stack, []int{forward, arr[forward]})
			arr[forward] = -1
		}
		if backward >= 0 && arr[backward] != -1 {
			if arr[backward] == 0 {
				return true
			}
			stack = append(stack, []int{backward, arr[backward]})
			arr[backward] = -1
		}
	}
	return false
}

// TC: O(n)
// SC: O(n)
func canReach2(arr []int, start int) bool {
	if arr[start] == 0 {
		return true
	}

	N := len(arr)
	dp := make([]bool, N)
	stack := make([][]int, 0, N)
	stack = append(stack, []int{start, arr[start]})
	dp[start] = true

	for len(stack) > 0 {
		node := stack[len(stack)-1]
		i, d := node[0], node[1]
		stack = stack[:len(stack)-1]

		forward, backward := i+d, i-d
		if forward < N && dp[forward] == false {
			if arr[forward] == 0 {
				return true
			}
			stack = append(stack, []int{forward, arr[forward]})
			dp[forward] = true
		}
		if backward >= 0 && dp[backward] == false {
			if arr[backward] == 0 {
				return true
			}
			stack = append(stack, []int{backward, arr[backward]})
			dp[backward] = true
		}
	}
	return false
}
