package leetcode

// Time complexity: O(n) where n is the length of word
// Space complexity: O(1)
func detectCapitalUse(word string) bool {
	return allLower(word) || allUpper(word) || capitalizedWord(word)
}

func allLower(word string) bool {
	for _, el := range word {
		if el < 'a' || el > 'z' {
			return false
		}
	}
	return true
}

func allUpper(word string) bool {
	for _, el := range word {
		if el < 'A' || el > 'Z' {
			return false
		}
	}
	return true
}

func capitalizedWord(word string) bool {
	if word[0] < 'A' || word[0] > 'Z' {
		return false
	}

	for i := 1; i < len(word); i++ {
		if word[i] < 'a' || word[i] > 'z' {
			return false
		}
	}
	return true
}
