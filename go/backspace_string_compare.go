package leetcode

// Time complexity: O(n + m) where n and m are the length of s and t
// Space complexity: O(n + m)
func backspaceCompare2(s string, t string) bool {
	build := func(s string) []byte {
		ss := make([]byte, 0, len(s))
		for i := 0; i < len(s); i++ {
			if s[i] == '#' && len(ss) > 0 {
				ss = ss[:len(ss)-1]
			} else if s[i] != '#' {
				ss = append(ss, s[i])
			}
		}
		return ss
	}

	ss, tt := build(s), build(t)
	if len(ss) != len(tt) {
		return false
	}

	for i := 0; i < len(ss); i++ {
		if ss[i] != tt[i] {
			return false
		}
	}
	return true

}
