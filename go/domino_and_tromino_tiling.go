package leetcode

// iterative dp solution
// TC: O(n)
// SC: O(1)
func numTilings(n int) int {
	dp := []int{1, 1, 2}
	if n <= 2 {
		return dp[n]
	}

	for i := 2; i < n; i++ {
		third, second, first := dp[0], dp[1], dp[2]
		dp[0], dp[1], dp[2] = second, first, (third+first*2)%1000000007
	}
	return dp[2]
}

// recursive solution with memoization
// TC: O(n)
// SC: O(n) for the recursive call stack and memoization
func numTilings2(n int) int {
	return solve(n, make(map[int]int))
}

func solve(n int, memo map[int]int) int {
	if n == 0 {
		return 1
	}
	if n <= 2 {
		return n
	}

	if val, ok := memo[n]; ok == true {
		return val
	}

	res := (2*solve(n-1, memo) + solve(n-3, memo)) % 1000000007
	memo[n] = res
	return res
}
