package leetcode

func hammingDistance(x int, y int) int {
	res := 0

	for x > 0 || y > 0 {
		res += (x ^ y) & 1
		x, y = x>>1, y>>1
	}
	return res
}
