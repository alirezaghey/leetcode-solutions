package leetcode

func uniquePaths(m int, n int) int {
	dp := make([]int, n)
	for i := 0; i < len(dp); i++ {
		dp[i] = 1
	}

	for i := 0; i < m-1; i++ {
		for j := 1; j < n; j++ {
			dp[j] = dp[j] + dp[j-1]
		}
	}

	return dp[len(dp)-1]
}
