package leetcode

func findKthNumber(m int, n int, k int) int {
	var distance func(x int) int
	distance = func(x int) int {
		cnt := 0
		for i := 1; i <= m; i++ {
			tmp := x / i
			if tmp < n {
				cnt += tmp
			} else {
				cnt += n
			}
		}
		return cnt
	}

	left, right := 1, m*n
	ans := 1

	for left <= right {
		mid := left + (right-left)/2
		d := distance(mid)

		if d >= k {
			ans = mid
			right = mid - 1
		} else {
			left = mid + 1
		}
	}

	return ans
}
