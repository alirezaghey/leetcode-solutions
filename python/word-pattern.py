class Solution:
    # Time complexity: O(n) where n is the number of words
    # Space complexity: O(n) where n is the number of words
    # Note: This is a slightly cleaner code written more pythonic
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(words) != len(pattern): return False
        
        w_to_p_mapping, p_to_w_mapping = dict(), dict()
        
        for w, p in zip(words, pattern):
            if w not in w_to_p_mapping and p not in p_to_w_mapping:
                w_to_p_mapping[w] = p
                p_to_w_mapping[p] = w
            elif w not in w_to_p_mapping or p not in p_to_w_mapping:
                return False
            elif w_to_p_mapping[w] != p or p_to_w_mapping[p] != w:
                return False
        return True
        
        
    # Time complexity: O(n) where n is the number of words
    # Space complexity: O(n)
    def wordPattern2(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(words) != len(pattern): return False
        w_to_p_mapping, p_to_w_mapping = dict(), dict()
        
        for i, word in enumerate(words):
            if word not in w_to_p_mapping:
                if pattern[i] in p_to_w_mapping:
                    return False
                w_to_p_mapping[word] = pattern[i]
                p_to_w_mapping[pattern[i]] = word
            if pattern[i] not in p_to_w_mapping or p_to_w_mapping[pattern[i]] != word or w_to_p_mapping[word] != pattern[i]:
                return False
        return True