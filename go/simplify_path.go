package leetcode

import "strings"

// Time complexity: O(n) where n the length of the input string is
// Space complexity: O(n)
func simplifyPath(path string) string {
	splitPath := strings.Split(path, "/")
	res := make([]string, 0)

	for _, p := range splitPath {
		if p == "" || p == "." {
			continue
		} else if p == ".." {
			if len(res) > 0 {
				res = res[:len(res)-1]
			}
		} else {
			res = append(res, p)
		}
	}

	return "/" + strings.Join(res, "/")
}
