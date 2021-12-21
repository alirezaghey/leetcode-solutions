package leetcode

// Time complexity: O(n) where n is the length of the input string
// Space complexity: O(n) since we need to create a runes array out of the input string
// Note: This is an optimization of the further below algorithm
// It works in one pass since we keep track of the character's indices
func lengthOfLongestSubstring(s string) int {
	left, maxSub := 0, 0
	seen := make(map[rune]int)
	sRunes := []rune(s)

	for right, el := range sRunes {
		if _, ok := seen[el]; ok == true {
			left = max(left, seen[el]+1)
		}
		seen[el] = right
		maxSub = max(maxSub, right-left+1)
	}
	return maxSub
}

// Time complexity: O(n) where n is the length of the input string
// Space complexity: O(n) since we need to create a runes array out of the input string
func lengthOfLongestSubstring2(s string) int {
	left, maxSub := 0, 0
	sRunes := []rune(s)
	have := make(map[rune]bool)

	for right, el := range sRunes {
		for {
			if _, ok := have[el]; ok == false {
				break
			}
			delete(have, sRunes[left])
			left += 1
		}
		have[el] = true
		maxSub = max(maxSub, right-left+1)
	}
	return maxSub
}

func max(x, y int) int {
	if x > y {
		return x
	} else {
		return y
	}
}
