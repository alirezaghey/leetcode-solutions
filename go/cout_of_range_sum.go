package leetcode

// Custom merge sort approach
func countRangeSum(nums []int, lower int, upper int) int {
	pref := make([]int, len(nums)+1)
	for i := 0; i < len(nums); i++ {
		pref[i+1] = pref[i] + nums[i]
	}

	var divide func(l, r int) int
	divide = func(l, r int) int {
		m := l + (r-l)/2
		if m == l {
			return 0
		}

		res := divide(l, m) + divide(m, r)

		i, j := m, m
		for _, left := range pref[l:m] {
			for i < r && pref[i]-left < lower {
				i += 1
			}
			for j < r && pref[j]-left <= upper {
				j += 1
			}
			res += j - i
		}

		temp := make([]int, m-l)
		copy(temp, pref[l:m])
		i, j, k := 0, m, l
		for i < len(temp) && j < r {
			if pref[j] < temp[i] {
				pref[k] = pref[j]
				k, j = k+1, j+1
			} else {
				pref[k] = temp[i]
				k, i = k+1, i+1
			}
		}

		for i < len(temp) {
			pref[k] = temp[i]
			k, i = k+1, i+1
		}
		for j < r {
			pref[k] = pref[j]
			k, j = k+1, j+1
		}
		return res
	}
	return divide(0, len(pref))
}
