package leetcode

func findNumOfValidWords(words []string, puzzles []string) []int {
	dic_words := make(map[int]int)
	for _, word := range words {
		mask := get_bit_mask(word)
		dic_words[mask] += 1
	}

	res := make([]int, len(puzzles))
	for i, puzzle := range puzzles {
		mask := get_bit_mask(puzzle)
		fst_letter := 1 << int(puzzle[0]-'a')
		count := 0
		subMask := mask
		for {
			if subMask&fst_letter != 0 {
				count += dic_words[subMask]
			}
			subMask = (subMask - 1) & mask
			if subMask == 0 {
				break
			}
		}
		res[i] = count
	}
	return res
}

func get_bit_mask(word string) int {
	res := 0
	for i := 0; i < len(word); i++ {
		res |= 1 << int(word[i]-'a')
	}
	return res
}
