package leetcode

// iterative dp solution
// TC: O(n * m) where n is length of nums and m is sum(nums)//2
// SC: O(m)
func canPartition(nums []int) bool {
	s := sum(nums)
	if s%2 != 0 {
		return false
	}
	half := s / 2
	dp := make([]bool, half+1)
	dp[half] = true

	for _, num := range nums {
		for el, state := range dp {
			if state == false {
				continue
			}
			new_el := el - num
			if new_el == 0 {
				return true
			}
			if new_el > 0 {
				dp[new_el] = true
			}
		}
	}
	return false
}

// recursive memoized solution
// TC: O(n * m) where n is length of nums and m is sum(nums)//2
// SC: O(n * m)
func canPartition2(nums []int) bool {
	s := sum(nums)
	if s%2 != 0 {
		return false
	}

	half := s / 2
	return dfs(0, half, make(map[State]bool), nums)
}

func dfs(idx, curr int, cache map[State]bool, nums []int) bool {
	if curr == 0 {
		return true
	}
	if idx >= len(nums) {
		return false
	}

	state := State{idx, curr}
	if val, ok := cache[state]; ok == true {
		return val
	}

	res := dfs(idx+1, curr-nums[idx], cache, nums) || dfs(idx+1, curr, cache, nums)
	cache[state] = res
	return res

}

func sum(nums []int) int {
	res := 0
	for _, el := range nums {
		res += el
	}
	return res
}

type State struct {
	idx  int
	curr int
}
