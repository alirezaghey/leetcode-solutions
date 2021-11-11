package leetcode

func shiftGrid(grid [][]int, k int) [][]int {
	var R, C int = len(grid), len(grid[0])
	k = k % (R * C)
	res := make([][]int, R)
	for i := range res {
		res[i] = make([]int, C)
	}

	for r := 0; r < R; r++ {
		for c := 0; c < C; c++ {
			res[(r+(c+k)/C)%R][(c+k)%C] = grid[r][c]
		}
	}
	return res
}
