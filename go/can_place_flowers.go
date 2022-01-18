package leetcode

// Time complexity: O(n) where n is the length of flowerbed
// Space complexity: O(1)
func canPlaceFlowers(flowerbed []int, n int) bool {
	if n == 0 {
		return true
	}

	prev := -1
	for i, el := range flowerbed {
		if el == 1 {
			prev = i
		} else if (prev == -1 || i-prev > 1) && (i == len(flowerbed)-1 || flowerbed[i+1] == 0) {
			n -= 1
			prev = i
			if n == 0 {
				return true
			}
		}
	}
	return false
}
