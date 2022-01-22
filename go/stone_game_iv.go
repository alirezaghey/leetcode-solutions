package leetcode

import (
	"math"
)

// Time complexity: O(sqrt(n) * n)
// Space complexity: O(n)
// Iterative bottom up solution
func winnerSquareGame(n int) bool {
	dp := make([]bool, n+1)
	for i := 1; i < n+1; i++ {
		upper := int(math.Sqrt(float64(i)))
		for j := upper; j > 0; j-- {
			if dp[i-j*j] == false {
				dp[i] = true
				break
			}
		}
	}
	return dp[len(dp)-1]
}

// Time complexity: O(sqrt(n) * n)
// Space complexity: O(n)
// Recursive top down solution
func winnerSquareGame2(n int) bool {
	var solve func(int, map[int]bool) bool
	solve = func(n int, memo map[int]bool) bool {
		if n == 0 {
			return false
		}

		if val, ok := memo[n]; ok == true {
			return val
		}

		upper := int(math.Sqrt(float64(n)))
		for i := upper; i > 0; i-- {
			if solve(n-i*i, memo) == false {
				memo[n] = true
				return true
			}
		}
		memo[n] = false
		return false
	}
	return solve(n, make(map[int]bool))
}
