package leetcode

// Time complexity: (n-k+1) + (n-k) + (n-k-1) + ... + (n-k-(n-k)) =>
//                  (n-k+1) + (n-k) + (n-k-1) + ... + (1) =>
//                  (1) + (2) + ... + (n-k+1) =>
//                  (n-k+1) * (n-k+2) / 2 =>
//                  O((n-k)^2)
// Space complexity: O((n-k)^2)
// Recursive backtracking solution
// Note: Optimized to bail out early
// if a path doesn't have the potential to lead to valid results
func combine(n int, k int) [][]int {
	res := make([][]int, 0, (n-k)*(n-k))
	partial_res := make([]int, 0, k)

	var backtrack func(curr int)
	backtrack = func(curr int) {
		if len(partial_res) == k {
			temp := make([]int, k)
			copy(temp, partial_res)
			res = append(res, temp)
		}

		for i := curr; i <= n; i++ {
			if k-len(partial_res) > n-curr+1 {
				continue
			}
			partial_res = append(partial_res, i)
			backtrack(i + 1)
			partial_res = partial_res[:len(partial_res)-1]
		}
	}

	backtrack(1)
	return res
}
