package leetcode

import "sort"

// Time complexity: O(n + m) where n and m are the length of the word arrays
// Space complexity: O(n) where n is the length of the start words
// Note about time and space complexity:
// We do (n * (s * log s + s)) operations to create the start_words dictionary
// where n is the number of start words and s is the maximum length of individual words
// since the length of a start word doesn't exceed 26 according to the input constraints
// the above calculation renders to (n * (26 * log 26 + 26))
// which reduces to n in big O terms
// the same goes for the space complexity and the target_words time and space complexity
func wordCount(startWords []string, targetWords []string) int {
	startWordsDic := make(map[string]map[rune]bool, len(startWords))

	for _, word := range startWords {
		charSet := make(map[rune]bool, len(word))
		for _, char := range []rune(word) {
			charSet[char] = true
		}
		startWordsDic[sortString(word)] = charSet
	}

	res := 0
	for _, targetWord := range targetWords {
		sortedTargetWord := sortString(targetWord)
		sortedTargetWordRunes := []rune(sortedTargetWord)

		for i, el := range sortedTargetWordRunes {
			tempTargetWord := string(sortedTargetWordRunes[:i]) + string(sortedTargetWordRunes[i+1:])
			if charSet, ok := startWordsDic[tempTargetWord]; ok == true {
				if _, ok := charSet[el]; ok == false {
					res += 1
					break
				}
			}
		}
	}
	return res
}

func sortString(input string) string {
	runeArray := []rune(input)
	sort.Sort(sortRuneString(runeArray))
	return string(runeArray)
}

type sortRuneString []rune

func (s sortRuneString) Swap(i, j int) {
	s[i], s[j] = s[j], s[i]
}

func (s sortRuneString) Less(i, j int) bool {
	return s[i] < s[j]
}

func (s sortRuneString) Len() int {
	return len(s)
}
