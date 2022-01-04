package leetcode

// Recursive top down approach
// Time complexity: O(R * C^2) where R is the number of rows and C is the number of columns of the grid
// Space complexity: O(R * C^2)
func cherryPickup(grid [][]int) int {
	R, C := len(grid), len(grid[0])
	memo := make([][][]int, R)

	for i := 0; i < len(memo); i++ {
		memo[i] = make([][]int, C)
		for j := 0; j < C; j++ {
			memo[i][j] = make([]int, C)
			for k := 0; k < C; k++ {
				memo[i][j][k] = -1
			}
		}
	}
	res := dfs(0, 0, C-1, memo, grid, R, C)
	return res
}

func dfs(r, c1, c2 int, memo [][][]int, grid [][]int, R int, C int) int {
	if r >= R {
		return 0
	}
	if c1 < 0 || c1 >= C || c2 < 0 || c2 >= C {
		return -10000
	}

	if memo[r][c1][c2] != -1 {
		return memo[r][c1][c2]
	}

	res := 0

	for i := -1; i < 2; i++ {
		for j := -1; j < 2; j++ {
			res = max(res, dfs(r+1, c1+i, c2+j, memo, grid, R, C))
		}
	}
	if c1 == c2 {
		res += grid[r][c1]
	} else {
		res += grid[r][c1] + grid[r][c2]
	}

	memo[r][c1][c2] = res
	return res
}

func max(x, y int) int {
	if x > y {
		return x
	} else {
		return y
	}
}
