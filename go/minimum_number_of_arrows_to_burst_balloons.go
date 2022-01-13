package leetcode

import (
	"sort"
)

// Time complexity: O(n * log n)
// Space complexity: O(1) or whatever the space complexity of the sorting algorithm is
func findMinArrowShots(points [][]int) int {
	sort.Slice(points, func(i, j int) bool { return points[i][0] < points[j][0] })

	var curr []int = nil
	res := 0
	for _, point := range points {
		if curr == nil {
			curr = point
		} else if point[0] <= curr[1] {
			curr = []int{max(point[0], curr[0]), min(point[1], curr[1])}
		} else {
			res += 1
			curr = point
		}
	}
	return res + 1
}

func min(x, y int) int {
	if x < y {
		return x
	} else {
		return y
	}
}

func max(x, y int) int {
	if x > y {
		return x
	} else {
		return y
	}
}
