package leetcode

// Time complexity: O(n) where n is the length of the seats array
// Space complexity: O(1)
// Note: It is crucial to take care of the edge cases of
// a prefix/suffix of empty seats in the seats array
func maxDistToClosest(seats []int) int {
	left, maxDist := -1, 1

	for right, el := range seats {
		if el == 0 {
			if left == -1 {
				maxDist = max(maxDist, right+1)
			} else {
				if (right-left)%2 == 0 {
					maxDist = max(maxDist, (right-left)/2)
				} else {
					maxDist = max(maxDist, (right-left+1)/2)
				}
			}
		} else {
			left = right
		}
	}
	if seats[len(seats)-1] == 0 {
		maxDist = max(maxDist, len(seats)-left-1)
	}
	return maxDist
}

func max(x, y int) int {
	if x > y {
		return x
	} else {
		return y
	}
}
