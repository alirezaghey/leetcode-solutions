package leetcode

import (
	"math"
)

// iterative bottom up approach with constant space
func checkRecord(n int) int {
	A := []int{1, 2}
	L := []int{1, 3}
	P := []int{1, 3}
	noAL := []int{1, 2}
	noAP := []int{1, 2}
	MOD := int(math.Pow(10, 9) + 7)

	if n < 3 {
		return A[n-1] + L[n-1] + P[n-1]
	}

	for i := 2; i < n; i++ {
		newA := []int{A[1], (noAL[1] + noAP[1]) % MOD}
		newNoAL := []int{noAL[1], (noAP[0] + noAP[1]) % MOD}
		newNoAP := []int{noAP[1], (noAP[1] + noAL[1]) % MOD}

		newL := []int{L[1], (A[1] + P[1] + A[0] + P[0]) % MOD}
		newP := []int{P[1], (A[1] + P[1] + L[1]) % MOD}

		A, L, P = newA, newL, newP
		noAL, noAP = newNoAL, newNoAP
	}

	return (A[1] + L[1] + P[1]) % MOD
}

// memoized recursive top down approache
func checkRecord2(n int) int {
	dp := make([][][]int, n+1)
	for i := 0; i < n+1; i++ {
		dp[i] = make([][]int, 3)
		for j := 0; j < 3; j++ {
			dp[i][j] = make([]int, 2)
		}
	}
	return dfs(n, 0, 0, dp)
}

func dfs(rem int, totalA int, continuousL int, memo [][][]int) int {
	if rem == 0 {
		return 1
	}

	if memo[rem][continuousL][totalA] != 0 {
		return memo[rem][continuousL][totalA]
	}

	mod := 1000000007
	res := 0
	if totalA == 0 {
		res = dfs(rem-1, 1, 0, memo)
		res %= mod
	}
	if continuousL < 2 {
		res += dfs(rem-1, totalA, continuousL+1, memo)
		res %= mod
	}
	res += dfs(rem-1, totalA, 0, memo)
	res %= mod

	memo[rem][continuousL][totalA] = res
	return res
}
