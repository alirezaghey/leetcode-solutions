# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Related Topics: Hash Table, Two Pointers, String, Sliding Window
# Difficulty: Medium


class Solution:
    # Time complexity: O(n) where n is the length of the input string
    # Space complexity: O(1) since the dictionary has never more than 26 elements
    # Note: This is an optimized version of the further down algorithm
    # Since it does only one pass
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_sub = 0
        left = 0
        have = dict()
        
        for right, el in enumerate(s):
            if el in have:
                left = max(left, have[el]+1)
            max_sub = max(max_sub, right - left + 1)
            have[el] = right
        return max_sub
    
    
    # Time complexity: O(n) where n is the length of the input string
    # Space complexity: O(1) since the set has never more than 26 elements
    def lengthOfLongestSubstring2(self, s: str) -> int:
        max_sub = 0
        left = 0
        have = set()
        
        for right, el in enumerate(s):
            while el in have:
                have.remove(s[left])
                left += 1
            have.add(el)
            max_sub = max(max_sub, right - left + 1)
        return max_sub

# Initial Thoughts:
# Using a Set and two pointers we are going to create a sliding window
# that stores all its values in the Set.
# Initially we start by advancing the right pointer and add the chars to
# the set. Each time we calculate the distance between the two pointers as
# the max substring without recurring chars and store it.
# Whenever we encounter a duplicate value, we remove the char that the left
# pointer is pointing to from the Set and move it forward until there is
# no duplicate. We repeat this until the left's distance to the end is no more
# than the max substring that we already found.

# Time complexity O(n) where n == len(s)
# Space complexity O(min(n,m)) where n == len(s) and m == len(charactersInAlphabet)
# We could also argue that the space complexity is constant since the number of characters
# in the alphabet is constant and well defined


class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mySet = set()
        max = 0
        left = right = 0
        while left < len(s)-max:
            if not s[right] in mySet:
                mySet.add(s[right])
                right += 1
                max = right - left if right - left > max else max
            else:
                mySet.remove(s[left])
                left += 1

        return max
