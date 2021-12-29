from typing import List


class Solution:
    # Time complexity: O(n + m) where n and m are the length of the word arrays
    # Space complexity: O(n) where n is the length of the start words
    # Note about time and space complexity:
    # We do (n * (s * log s + s)) operations to create the start_words dictionary
    # where n is the number of start words and s is the maximum length of individual words
    # since the length of a start word doesn't exceed 26 according to the input constraints
    # the above calculation renders to (n * (26 * log 26 + 26))
    # which reduces to n in big O terms
    # the same goes for the space complexity and the target_words time and space complexity
    def wordCount(self, start_words: List[str], target_words: List[str]) -> int:
        start_words = {"".join(list(sorted(word))): set(word) for word in start_words}
        
        res = 0
        for target_word in target_words:
            sorted_t_word = "".join(list(sorted(target_word)))
            for i, el in enumerate(sorted_t_word):
                temp_sorted_t_word = sorted_t_word[:i] + sorted_t_word[i+1:]
                if  temp_sorted_t_word in start_words and el not in start_words[temp_sorted_t_word]:
                    res += 1
                    break

        return res