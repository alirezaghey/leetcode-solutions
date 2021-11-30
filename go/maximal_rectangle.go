package leetcode

func maximalRectangle(matrix [][]byte) int {
	R := len(matrix)
	if R == 0 {
		return 0
	}
	C := len(matrix[0])

	dp := make([][]int, R)
	for r := 0; r < R; r++ {
		dp[r] = make([]int, C)
	}

	for r := 0; r < R; r++ {
		for c := 0; c < C; c++ {
			if matrix[r][c] == '0' {
				continue
			}
			if c > 0 {
				dp[r][c] = 1 + dp[r][c-1]
			} else {
				dp[r][c] = 1
			}
		}
	}

	res := 0
	for c := 0; c < C; c++ {
		for r := 0; r < R; r++ {
			curr, count := 0, 0
			for r1 := r; r1 < R; r1++ {
				if curr == 0 {
					if dp[r1][c] == 0 {
						break
					} else {
						curr = dp[r1][c]
						count = 1
						if curr > res {
							res = curr
						}
					}
				} else {
					if dp[r1][c] == 0 {
						curr = 0
						count = 0
						break
					} else {
						if dp[r1][c] > res {
							res = dp[r1][c]
						}
						if dp[r1][c] < curr {
							curr = dp[r1][c]
						}
						count++
						if count*curr > res {
							res = count * curr
						}
					}
				}
			}
		}
	}
	return res
}
