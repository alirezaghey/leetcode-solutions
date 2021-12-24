package leetcode

import "sort"

func merge(intervals [][]int) [][]int {
	sort.Slice(intervals, func(i, j int) bool {
		for x := range intervals[i] {
			if intervals[i][x] == intervals[j][x] {
				continue
			}
			return intervals[i][x] < intervals[j][x]
		}
		return false
	})
	res := make([][]int, 1)
	res[0] = intervals[0]
	for i := 1; i < len(intervals); i++ {
		if intervals[i][0] <= res[len(res)-1][1] {
			res[len(res)-1][1] = max(res[len(res)-1][1], intervals[i][1])
		} else {
			res = append(res, intervals[i])
		}
	}
	return res
}

func max(x, y int) int {
	if x > y {
		return x
	} else {
		return y
	}
}
