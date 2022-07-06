
// TC: O(n)
// SC: O(1)
const fib = function (n: number): number {
    const dp = [0, 1]

    if (n < 2) return dp[n]
    for (let i = 0; i < n - 1; i++)
        [dp[0], dp[1]] = [dp[1], dp[0] + dp[1]]

    return dp[1]
};