package leetcode

func commonChars(words []string) []string {
	word_dic := make([]map[rune]int, len(words))

	for i, word := range words {
		m := make(map[rune]int)
		for _, c := range word {
			m[c] += 1
		}
		word_dic[i] = m
	}

	var res []string
	for key, val := range word_dic[0] {
		curr := val
		for i := 1; i < len(word_dic); i++ {
			if word_dic[i][key] < curr {
				curr = word_dic[i][key]
				if curr == 0 {
					break
				}
			}
		}
		for i := 0; i < curr; i++ {
			res = append(res, string(key))
		}
	}
	return res

}
