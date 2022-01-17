package leetcode

// Time complexity: O(n * m) where n and m are the rows and columns of the matrix
// Space complexity: O(n * m)
// DFS approach
func floodFill(image [][]int, sr int, sc int, newColor int) [][]int {
	if image[sr][sc] == newColor {
		return image
	}
	dfs(image, sr, sc, image[sr][sc], newColor, len(image), len(image[0]))
	return image
}

func dfs(image [][]int, r, c, startColor, newColor, R, C int) {
	image[r][c] = newColor

	if r-1 >= 0 && image[r-1][c] == startColor {
		dfs(image, r-1, c, startColor, newColor, R, C)
	}
	if c+1 < C && image[r][c+1] == startColor {
		dfs(image, r, c+1, startColor, newColor, R, C)
	}
	if r+1 < R && image[r+1][c] == startColor {
		dfs(image, r+1, c, startColor, newColor, R, C)
	}
	if c-1 >= 0 && image[r][c-1] == startColor {
		dfs(image, r, c-1, startColor, newColor, R, C)
	}
}

// Time complexity: O(n * m) where n and m are the rows and columns of the matrix
// Space complexity: O(n * m)
// BFS approach
func floodFill2(image [][]int, sr int, sc int, newColor int) [][]int {
	R, C := len(image), len(image[0])
	startColor := image[sr][sc]

	if startColor == newColor {
		return image
	}

	stack := [][]int{{sr, sc}}
	image[sr][sc] = newColor
	dirs := [][]int{{-1, 0}, {0, 1}, {1, 0}, {0, -1}}
	for len(stack) > 0 {
		node := stack[len(stack)-1]
		r, c := node[0], node[1]
		stack = stack[:len(stack)-1]

		for _, d := range dirs {
			dr, dc := d[0], d[1]
			nr, nc := r+dr, c+dc

			if nr >= 0 && nr < R && nc >= 0 && nc < C && image[nr][nc] == startColor {
				stack = append(stack, []int{nr, nc})
				image[nr][nc] = newColor
			}
		}
	}
	return image
}
