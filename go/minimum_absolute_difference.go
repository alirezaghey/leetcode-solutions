package leetcode

import (
	"math"
	"sort"
)

func minimumAbsDifference(arr []int) [][]int {
	sort.Ints(arr)
	res := make([][]int, 0, 10)
	min_diff := int(math.Abs(float64(arr[0] - arr[1])))

	for i := 1; i < len(arr); i++ {
		min_diff = min(min_diff, int(math.Abs(float64(arr[i]-arr[i-1]))))
	}

	for i := 1; i < len(arr); i++ {
		if int(math.Abs(float64(arr[i]-arr[i-1]))) == min_diff {
			res = append(res, []int{arr[i-1], arr[i]})
		}
	}

	return res
}

func min(x, y int) int {
	if x < y {
		return x
	} else {
		return y
	}
}
