package leetcode

func maxSubArray(nums []int) int {
	res := nums[0]
	for i := 1; i < len(nums); i++ {
		if nums[i-1] > 0 {
			nums[i] += nums[i-1]
		}
		if nums[i] > res {
			res = nums[i]
		}
	}
	return res
}

// Using divide and conquer approach
func maxSubArray2(nums []int) int {
	return dAndd(0, len(nums)-1, nums)
}

func dAndd(l, r int, nums []int) int {
	if l == r {
		return nums[l]
	}

	m := l + (r-l)/2
	left := dAndd(l, m, nums)
	right := dAndd(m+1, r, nums)

	lMax, curr := nums[m], nums[m]
	for i := m - 1; i >= l; i-- {
		curr += nums[i]
		if curr > lMax {
			lMax = curr
		}
	}

	rMax, curr := 0, 0
	for i := m + 1; i <= r; i++ {
		curr += nums[i]
		if curr > rMax {
			rMax = curr
		}
	}

	if left >= right && left >= lMax+rMax {
		return left
	} else if right >= left && right >= lMax+rMax {
		return right
	} else {
		return lMax + rMax
	}
}
