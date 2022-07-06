/**
 * @param {number} n
 * @return {number}
 */

// TC: O(n)
// SC: O(1)
var fib = function (n) {
    const dp = [0, 1]
    if (n < 2) return dp[n]

    for (i = 0; i < n - 1; i++)
        [dp[0], dp[1]] = [dp[1], dp[0] + dp[1]]

    return dp[1]
};