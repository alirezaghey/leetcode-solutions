package leetcode

func countSmaller(nums []int) []int {
	newNums := make([][]int, len(nums))

	for i, el := range nums {
		newNums[i] = []int{i, el}
	}

	res := make([]int, len(nums))
	divide(0, len(nums)-1, newNums, res)
	return res
}

func divide(l, r int, nums [][]int, res []int) {
	if l >= r {
		return
	}

	m := l + (r-l)/2
	divide(l, m, nums, res)
	divide(m+1, r, nums, res)

	i, j := l, m+1
	for i <= m {
		for j <= r && nums[j][1] < nums[i][1] {
			j++
		}
		res[nums[i][0]] += j - m - 1
		i++
	}

	merge(l, r, m, nums)
}
func merge(l, r, m int, nums [][]int) {
	i, j, k := 0, m+1, l
	temp := make([][]int, m-l+1)
	copy(temp, nums[l:m+1])

	for i < len(temp) && j <= r {
		if temp[i][1] <= nums[j][1] {
			nums[k] = temp[i]
			i++
		} else {
			nums[k] = nums[j]
			j++
		}
		k++
	}

	for i < len(temp) {
		nums[k] = temp[i]
		k++
		i++
	}

	for j <= r {
		nums[k] = nums[j]
		k++
		j++
	}
}
