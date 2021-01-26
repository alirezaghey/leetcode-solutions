package leetcode

func nthMagicalNumber(n int, a int, b int) int {
	lower, upper := min(a, b), n*a
	best := upper
	leastCommonMul := lcm(a, b)
	MOD := 1_000_000_007

	for lower <= upper {
		mid := lower + (upper-lower)/2
		curr := mid/a + mid/b - mid/leastCommonMul

		if curr >= n {
			best = min(best, mid)
			upper = mid - 1
		} else {
			lower = mid + 1
		}
	}
	return best % MOD
}

func min(x, y int) int {
	if x < y {
		return x
	} else {
		return y
	}
}
func lcm(x, y int) int {
	x1, y1 := x, y

	for x1 != y1 {
		if x1 < y1 {
			x1 += x
		} else {
			y1 += y
		}
	}
	return x1
}
