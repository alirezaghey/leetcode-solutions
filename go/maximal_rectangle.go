package leetcode

/*
Approach:
Using the max area rectangle in skyline approach
with a mono stack
*/
func maximalRectangle(matrix [][]byte) int {
	R := len(matrix)
	if R == 0 {
		return 0
	}
	C := len(matrix[0])

	dp := make([][]int, R)
	for r := 0; r < R; r++ {
		dp[r] = make([]int, C+1)
	}

	for c := 0; c < C; c++ {
		curr := 0
		for r := 0; r < R; r++ {
			if matrix[r][c] == '0' {
				curr = 0
				continue
			}
			curr++
			dp[r][c] = curr
		}
	}

	res := 0
	for r := 0; r < R; r++ {
		stack := []int{}
		for c := 0; c < C+1; c++ {
			for len(stack) > 0 && dp[r][stack[len(stack)-1]] >= dp[r][c] {
				h := dp[r][stack[len(stack)-1]]
				stack = stack[:len(stack)-1]
				var w int
				if len(stack) > 0 {
					w = c - stack[len(stack)-1] - 1
				} else {
					w = c
				}
				if w*h > res {
					res = w * h
				}
			}
			stack = append(stack, c)
		}
	}
	return res
}

/*
Approach:
Create dp where dp[i][j] is the sum of continues 1s to the left in row i including for j itself
For each column of the dp, for each row, look for continues rows without zero, take their min times the count of rows
That's the maximum area we can achieve
Note that we need to start at each row once
Also, we can break if we find a row that is zero
*/
func maximalRectangle2(matrix [][]byte) int {
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
