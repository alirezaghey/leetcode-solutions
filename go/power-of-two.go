package leetcode

func isPowerOfTwo(n int) bool {
	if n <= 0 {
		return false
	}

	found := false
	for n > 0 {
		if n&1 == 1 {
			if found {
				return false
			} else {
				found = true
			}
		}
		n >>= 1
	}
	return true
}
func isPowerOfTwo2(n int) bool {
	return n > 0 && ((n-1)&n) == 0
}
