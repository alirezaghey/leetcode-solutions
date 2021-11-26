package leetcode

func twoSum(nums []int, target int) []int {
	dic := make(map[int]int)
	var res []int

	for i, el := range nums {
		if idx, ok := dic[target-el]; ok {
			res = []int{idx, i}
			break
		}
		dic[el] = i
	}
	return res
}
