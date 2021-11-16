package leetcode

import (
	"sort"
)

func largestDivisibleSubset(nums []int) []int {
	if len(nums) == 0 {
		return []int{}
	}
	sort.Ints(nums)
	dp := make([][]int, len(nums))
	for i, el := range nums {
		dp[i] = []int{el}
	}
	for i := 0; i < len(nums); i++ {
		for j := 0; j < i; j++ {
			if nums[i]%nums[j] == 0 && len(dp[i]) < len(dp[j])+1 {
				new_ := make([]int, len(dp[j])+1)
				copy(new_, dp[j])
				new_[len(new_)-1] = nums[i]
				dp[i] = new_
			}
		}
	}
	res := dp[0]
	for i := 1; i < len(dp); i++ {
		if len(dp[i]) > len(res) {
			res = dp[i]
		}
	}
	return res
}
