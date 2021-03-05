package leetcode

func maxPower(s string) int {
	best, curr_count, curr_char := 0, 0, '#'

	for _, el := range []rune(s) {
		if el == curr_char {
			curr_count += 1
		} else {
			curr_char = el
			curr_count = 1
		}
		best = max(best, curr_count)
	}
	return best
}

func max(x, y int) int {
	if x > y {
		return x
	} else {
		return y
	}
}
