package leetcode

// Time complexity: O(n)
// Space complexity: O(1)
func validPalindrome(s string) bool {

	return check(0, len(s)-1, s, false)
}

func check(left, right int, s string, found bool) bool {
	for left < right {
		if s[left] != s[right] {
			if found == true {
				return false
			} else {
				return check(left+1, right, s, true) || check(left, right-1, s, true)
			}
		} else {
			left++
			right--
		}
	}
	return true
}
