package leetcode

// Time complexity: O(n) where n is the length of nums
// Space complexity: O(n)
func subarraySum(nums []int, k int) int {
	dic := make(map[int]int)
	dic[0] = 1
	curr, res := 0, 0

	for _, el := range nums {
		curr += el
		if val, ok := dic[curr-k]; ok == true {
			res += val
		}
		if val, ok := dic[curr]; ok == true {
			dic[curr] = val + 1
		} else {
			dic[curr] = 1
		}
	}
	return res
}
