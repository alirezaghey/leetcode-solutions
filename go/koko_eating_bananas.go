package leetcode

import (
	"math"
	"sort"
)

// Time comlexity: O(n * log n + log m * log n * n) where n is the length of piles
// and m is max(piles)
// Space complexity: O(1) or whatever space the sorting algorithm needs
// Note: Sorting piles is not necessary for AC
// It is better or worse than an algorithm where you don't sort piles
// depending on the length of piles
// If piles is big enough in comparison to its max value sorting makes much more sense
func minEatingSpeed(piles []int, h int) int {
	sort.Ints(piles)
	l, r := 1, piles[len(piles)-1]
	res := r

	for l <= r {
		mid := l + (r-l)/2
		idx := bisectRight(piles, mid)
		curr := idx

		for i := curr; i < len(piles); i++ {
			curr += int(math.Ceil(float64(piles[i]) / float64(mid)))
			if curr > h {
				break
			}
		}
		if curr > h {
			l = mid + 1
		} else {
			if mid < res {
				res = mid
			}
			r = mid - 1
		}
	}
	return res
}

func bisectRight(arr []int, el int) int {
	l, r := 0, len(arr)

	for l < r {
		mid := l + (r-l)/2
		if el < arr[mid] {
			r = mid
		} else {
			l = mid + 1
		}
	}
	return l
}

// Time complexity: O(n * log m) where n is length of piles and m is max(piles)
// Space complexity: O(1)
func minEatingSpeed2(piles []int, h int) int {
	l, r := 1, max(piles)
	res := r

	for l <= r {
		mid := l + (r-l)/2
		curr := 0
		for _, el := range piles {
			curr += int(math.Ceil(float64(el) / float64(mid)))
			if curr > h {
				break
			}
		}
		if curr > h {
			l = mid + 1
		} else {
			if mid < res {
				res = mid
			}
			r = mid - 1
		}
	}
	return res
}

func max(arr []int) int {
	res := arr[0]
	for _, el := range arr {
		if el > res {
			res = el
		}
	}
	return res
}
