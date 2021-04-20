package leetcode

func maximalSquare(matrix [][]byte) int {
	R, C := len(matrix), len(matrix[0])
	dp := make([][]int, R+1)
	for r := 0; r < R+1; r++ {
		dp[r] = make([]int, C+1)
	}

	best := 0
	for r := 0; r < R; r++ {
		for c := 0; c < C; c++ {
			if matrix[r][c] == '1' {
				dp[r+1][c+1] = min(dp[r][c], min(dp[r][c+1], dp[r+1][c])) + 1
				best = max(best, dp[r+1][c+1])
			}
		}
	}
	return best * best
}

func min(x, y int) int {
	if x < y {
		return x
	} else {
		return y
	}
}

func max(x, y int) int {
	if x > y {
		return x
	} else {
		return y
	}
}
