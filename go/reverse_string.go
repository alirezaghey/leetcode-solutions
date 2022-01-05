package leetcode

// Time complexity: O(n) where n is the length of the input array
// Space complexity: O(1)
func reverseString(s []byte) {
	N := len(s)
	for i := 0; i < N/2; i++ {
		s[i], s[N-1-i] = s[N-1-i], s[i]
	}
}
