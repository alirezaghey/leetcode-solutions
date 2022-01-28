package leetcode

// Time complexity: O(n + m) where n and m are the lengths of s and t
// Space complexity: O(1)
func backspaceCompare(s string, t string) bool {
	i, j := len(s)-1, len(t)-1

	for i >= 0 || j >= 0 {
		c := 0
		for i >= 0 && (s[i] == '#' || c > 0) {
			if s[i] == '#' {
				c++
			} else {
				c--
			}
			i--
		}

		c = 0
		for j >= 0 && (t[j] == '#' || c > 0) {
			if t[j] == '#' {
				c++
			} else {
				c--
			}
			j--
		}

		if i >= 0 && j >= 0 {
			if s[i] != t[j] {
				return false
			}
		} else {
			break
		}
		i--
		j--
	}
	return i < 0 && j < 0
}

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
