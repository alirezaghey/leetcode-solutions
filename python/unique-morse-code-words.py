from typing import List


class Solution:
    # TC: O(n * m) where n is the number of words and m is the max length of the words
    # SC: O(n * m)
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
                "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        res = set()

        for word in words:
            curr = []
            for c in word:
                curr.append(code[ord(c) - ord('a')])
            res.add("".join(curr))

        return len(res)
