package leetcode

func singleNumber(nums []int) []int {
	xor := 0
	for _, el := range nums {
		xor ^= el
	}

	mask := 1
	for mask&xor == 0 {
		mask <<= 1
	}

	a, b := 0, 0
	for _, el := range nums {
		if mask&el == 0 {
			a ^= el
		} else {
			b ^= el
		}
	}

	return []int{a, b}
}
