package leetcode

import (
	"math"
)

func reverse(x int) int {
	var sign int
	if x < 0 {
		sign = -1
	} else {
		sign = 1
	}

	x = int(math.Abs(float64(x)))
	res := 0
	lower, upper := int(math.Pow(-2, 31)), int(math.Pow(2, 31)-1)

	for x > 0 {
		res *= 10
		res += x % 10
		x /= 10
		if res < lower || res > upper {
			return 0
		}
	}
	return res * sign
}
