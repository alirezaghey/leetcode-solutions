package leetcode

// Time complexity: O(n * m) where n and m are the rows and columns of the grid
// Space complexity: O(n * m)
// DFS
func maxAreaOfIsland(grid [][]int) int {
	R, C := len(grid), len(grid[0])
	res := 0

	for r := 0; r < R; r++ {
		for c := 0; c < C; c++ {
			if grid[r][c] == 1 {
				res = max(res, dfs(grid, r, c, R, C)+1)
			}
		}
	}
	return res
}

func dfs(grid [][]int, r, c, R, C int) int {
	grid[r][c] = 0

	res := 0
	if r-1 >= 0 && grid[r-1][c] == 1 {
		res += dfs(grid, r-1, c, R, C) + 1
	}
	if c+1 < C && grid[r][c+1] == 1 {
		res += dfs(grid, r, c+1, R, C) + 1
	}
	if r+1 < R && grid[r+1][c] == 1 {
		res += dfs(grid, r+1, c, R, C) + 1
	}
	if c-1 >= 0 && grid[r][c-1] == 1 {
		res += dfs(grid, r, c-1, R, C) + 1
	}
	return res
}

// Time complexity: O(n * m) where n and m are the rows and columns of the grid
// Space complexity: O(n * m)
// BFS
// Note: Due to the use of a slice for a queue the effective time complexity of this algorithm
// could become quadratic in the number of nodes
func maxAreaOfIsland2(grid [][]int) int {
	R, C := len(grid), len(grid[0])
	res := 0

	for r := 0; r < R; r++ {
		for c := 0; c < C; c++ {
			if grid[r][c] == 1 {
				res = max(res, bfs(grid, r, c, R, C))
			}
		}
	}
	return res
}

func bfs(grid [][]int, r, c, R, C int) int {
	dirs := [][]int{{-1, 0}, {0, 1}, {1, 0}, {0, -1}}
	queue := [][]int{{r, c}}
	grid[r][c] = 0
	res := 1

	for len(queue) > 0 {
		node := queue[0]
		r, c := node[0], node[1]
		queue = queue[1:]

		for _, d := range dirs {
			dr, dc := d[0], d[1]
			nr, nc := r+dr, c+dc

			if nr >= 0 && nr < R && nc >= 0 && nc < C && grid[nr][nc] == 1 {
				res += 1
				grid[nr][nc] = 0
				queue = append(queue, []int{nr, nc})
			}
		}
	}
	return res
}

func max(x, y int) int {
	if x > y {
		return x
	} else {
		return y
	}
}
