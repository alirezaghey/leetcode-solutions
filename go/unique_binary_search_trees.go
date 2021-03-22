func numTrees(n int) int {
    dp := []int{1, 1, 2}
    if n < 3 {
        return dp[n]
    }
    
    for i := 3; i < n+1; i++ {
        curr := 0
        for j := 1; j < i+1; j++ {
            curr += dp[j-1]*dp[i-j]
        }
        dp = append(dp, curr)
    }
    return dp[len(dp)-1]
}