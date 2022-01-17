package leetcode

import (
	"strings"
)

func wordPattern(pattern string, s string) bool {
	words := strings.Split(s, " ")
	if len(words) != len(pattern) {
		return false
	}

	wToPMapping, pToWMapping := make(map[string]byte), make(map[byte]string)

	for i := 0; i < len(words); i++ {
		w, p := words[i], pattern[i]
		pW, wOk := wToPMapping[w]
		wP, pOk := pToWMapping[p]

		if wOk == false && pOk == false {
			wToPMapping[w] = p
			pToWMapping[p] = w
		} else if wOk == false || pOk == false {
			return false
		} else if pW != p || wP != w {
			return false
		}
	}
	return true
}
