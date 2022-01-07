package leetcode

func isRobotBounded(instructions string) bool {
	x, y, dir := 0, 0, 0
	directions := [][]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}}

	for _, instruction := range []rune(instructions) {
		if instruction == 'R' {
			dir = (dir + 1) % 4
		} else if instruction == 'L' {
			dir = (dir + 3) % 4
		} else {
			x, y = x+directions[dir][0], y+directions[dir][1]
		}
	}

	return (x == 0 && y == 0) || dir != 0
}
