package leetcode

// iterative dp solution
// TC: O(n)
// SC: O(1)
func maxProduct(nums []int) int {
	n := len(nums)
	var res data
	if nums[n-1] < 0 {
		res = data{nums[n-1], 0}
	} else {
		res = data{0, nums[n-1]}
	}

	best := nums[n-1]
	for i := n - 2; i >= 0; i-- {
		if nums[i] == 0 {
			res.negative, res.positive = 0, 0
		} else if nums[i] < 0 {
			res.negative, res.positive = min(nums[i], res.positive*nums[i]), res.negative*nums[i]
		} else {
			res.negative, res.positive = res.negative*nums[i], max(nums[i], res.positive*nums[i])
		}
		best = max(best, res.positive)
	}
	return best
}

// iterative dp solution
// TC: O(n)
// SC: O(n)
func maxProduct2(nums []int) int {
	n := len(nums)
	dp := make([]data, n)
	if nums[n-1] < 0 {
		dp[n-1] = data{nums[n-1], 0}
	} else {
		dp[n-1] = data{0, nums[n-1]}
	}

	best := nums[n-1]
	for i := n - 2; i >= 0; i-- {
		if nums[i] == 0 {
			dp[i] = data{0, 0}
		} else if nums[i] < 0 {
			dp[i] = data{min(dp[i+1].positive*nums[i], nums[i]), nums[i] * dp[i+1].negative}
		} else {
			dp[i] = data{dp[i+1].negative * nums[i], max(nums[i]*dp[i+1].positive, nums[i])}
		}
		best = max(best, dp[i].positive)
	}
	return best
}

type data struct {
	negative int
	positive int
}

func max(x, y int) int {
	if x > y {
		return x
	} else {
		return y
	}
}

func min(x, y int) int {
	if x < y {
		return x
	} else {
		return y
	}
}
