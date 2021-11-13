package leetcode

func dailyTemperatures(temperatures []int) []int {
	res := make([]int, len(temperatures))
	stack := make([]int, 0)

	for i, el := range temperatures {
		for len(stack) > 0 && el > temperatures[stack[len(stack)-1]] {
			j := stack[len(stack)-1]
			res[j] = i - j
			stack = stack[:len(stack)-1]
		}
		stack = append(stack, i)
	}
	return res

}
