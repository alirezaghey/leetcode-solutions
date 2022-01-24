class Solution:
    # Note about space complexity of all the below algorithms:
    # All of them are in fact O(n) because of word[1:] which makes
    # a copy of word dropping the first character
    # This can be avoided by just looping over those characters
    
    # Time complexity: O(n) where n is the length of word
    # Space complexity: O(1)
    def detectCapitalUse(self, word: str) -> bool:
        return (
            all(map(lambda c: ord('a') <= ord(c) <= ord('z'), word)) or
            all(map(lambda c: ord('A') <= ord(c) <= ord('Z'), word)) or
            (
                ord('A') <= ord(word[0]) <= ord('Z') and
                all(map(lambda c: ord('a') <= ord(c) <= ord('z'), word[1:]))
            )
        )
    # Time complexity: O(n) where n is the length of word
    # Space complexity: O(1)
    def detectCapitalUse2(self, word: str) -> bool:
        return word.islower() or word.isupper() or (word[0].isupper() and word[1:].islower())
    
    
    # Time complexity: O(n) where n is the length of word
    # Space complexity: O(1)
    def detectCapitalUse3(self, word: str) -> bool:
        return all(map(str.islower, word)) or all(map(str.isupper, word)) or (word[0].isupper() and word[1:].islower())