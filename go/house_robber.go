package leetcode

// iterative solution
// TC: O(n)
// SC: O(1)
func rob(nums []int) int {
	var max func(x, y int) int
	max = func(x, y int) int {
		if x > y {
			return x
		} else {
			return y
		}
	}

	taken, notTaken := nums[0], 0
	for i := 1; i < len(nums); i++ {
		taken, notTaken = notTaken+nums[i], max(notTaken, taken)
	}
	return max(taken, notTaken)
}

// iterative solution
// TC: O(n)
// SC: O(n)
func rob2(nums []int) int {
	dp := make([][]int, len(nums))
	dp[0] = []int{nums[0], 0}
	for i := 1; i < len(nums); i++ {
		dp[i] = make([]int, 2)
		dp[i][0] = dp[i-1][1] + nums[i]
		if dp[i-1][0] > dp[i-1][1] {
			dp[i][1] = dp[i-1][0]
		} else {
			dp[i][1] = dp[i-1][1]
		}
	}
	if dp[len(dp)-1][0] > dp[len(dp)-1][1] {
		return dp[len(dp)-1][0]
	} else {
		return dp[len(dp)-1][1]
	}
}

// recursive memoized solution
// TC: O(n) where n is the length of nums
// SC: O(n)
func rob3(nums []int) int {
	cache := make([]Cache, len(nums))
	var dfs func(idx int, taken bool) int
	dfs = func(idx int, taken bool) int {
		if idx >= len(nums) {
			return 0
		}
		if taken && cache[idx].taken != nil {
			return *cache[idx].taken
		}
		if !taken && cache[idx].notTaken != nil {
			return *cache[idx].notTaken
		}

		if taken {
			num := dfs(idx+1, false)
			cache[idx].taken = &num
			return *cache[idx].taken
		} else {
			take := dfs(idx+1, true) + nums[idx]
			dontTake := dfs(idx+1, false)
			if take > dontTake {
				cache[idx].notTaken = &take
			} else {
				cache[idx].notTaken = &dontTake
			}
			return *cache[idx].notTaken
		}

	}
	dfs(0, false)
	return *cache[0].notTaken
}

type Cache struct {
	taken    *int
	notTaken *int
}
