package leetcode

// Time complexity: O(n) where n is the length of the input string
// Space complexity: O(n) for the additional runes array
// Note that the algorithm is in-place but since Go strings are
// immutable we have to convert them to an array
func reverseWords(s string) string {
	reverse := func(runes []rune, l, r int) {
		for i := 0; i < (r-l+1)/2; i++ {
			runes[l+i], runes[r-i] = runes[r-i], runes[l+i]
		}
	}

	sRunes := []rune(s)
	l := -1
	for i := range sRunes {
		if i == len(sRunes)-1 || sRunes[i+1] == ' ' {
			if l == -1 {
				l = i
			}
			reverse(sRunes, l, i)
			l = -1
		} else if sRunes[i] != ' ' && l == -1 {
			l = i
		}
	}
	return string(sRunes)
}
