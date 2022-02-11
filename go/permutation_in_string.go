package leetcode

// Time complexity: O(n) where n is the length of s2
// Space complexity: O(1) since the dictionaries will never have more than 26 members
func checkInclusion(s1 string, s2 string) bool {
	createFreqTable := func(s string) map[rune]int {
		dic := make(map[rune]int)
		for _, char := range []rune(s) {
			val, ok := dic[char]
			if ok == true {
				dic[char] = val + 1
			} else {
				dic[char] = 1
			}
		}
		return dic
	}

	compareDics := func(dic1 map[rune]int, dic2 map[rune]int) bool {
		for k1, v1 := range dic1 {
			v2, ok := dic2[k1]
			if ok == false || v2 != v1 {
				return false
			}
		}

		for k2, v2 := range dic2 {
			v1, ok := dic1[k2]
			if ok == false || v1 != v2 {
				return false
			}
		}
		return true
	}

	if len(s2) < len(s1) {
		return false
	}

	freqTable := createFreqTable(s1)
	currTable := createFreqTable(s2[:len(s1)])

	if compareDics(freqTable, currTable) {
		return true
	}

	for i := len(s1); i < len(s2); i++ {
		char := rune(s2[i])
		if val, ok := currTable[char]; ok == true {
			currTable[char] = val + 1
		} else {
			currTable[char] = 1
		}

		char = rune(s2[i-len(s1)])

		if val, _ := currTable[char]; val == 1 {
			delete(currTable, char)
		} else {
			currTable[char] = val - 1
		}
		if compareDics(freqTable, currTable) {
			return true
		}
	}
	return false
}
