package leetcode

// Time complexity: O(log num)
// Space complexity: O(1)
func addDigits(num int) int {
	add := func(num int) int {
		res := 0
		for num > 0 {
			res += num % 10
			num /= 10
		}
		return res
	}

	for num > 9 {
		num = add(num)
	}
	return num
}
