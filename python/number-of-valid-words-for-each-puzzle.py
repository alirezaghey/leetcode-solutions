import collections

class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        def get_bit_mask(word):
            mask = 0
            for c in word:
                mask |= 1 << (ord(c) - ord('a'))
            return mask
        
        counter_words = collections.Counter()
        for word in words:
            mask = get_bit_mask(word)
            counter_words[mask] += 1
        
        res = []
        for puzzle in puzzles:
            count = 0
            fst_letter = 1 << (ord(puzzle[0]) - ord('a'))
            mask = get_bit_mask(puzzle)
            sub_mask = mask
            while True:
                if sub_mask & fst_letter:
                    count += counter_words[sub_mask]
                sub_mask = (sub_mask - 1) & mask
                if sub_mask == 0:
                    break
            res.append(count)
        return res