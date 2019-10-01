#  https://leetcode.com/problems/intersection-of-two-arrays/
#  Related Topics: Hash Table, Two Pointers, Binary Search, Sort
#  Difficulty: Easy


# Initial thoughts:
# Using a hash table we are going to add every element of the first array to it.
# Now, looping over the second array, if we find that an element is available in
# the previously created hash table, we are going to add that element to another
# hash table that will hold the intersection of the two arrays. The use of the
# second hash table to the end result is due to the fact that we want to avoid
# duplicate values in our end results.
# Another way of doing this would be to create a second hash table for the second
# array and compare its values with our first hashtable. This way there won't be
# any duplicate results in the first place. There is no difference between the two
# approaches in terms of space and time complexity, while the first approach could
# potentially save some space.


# Time complexity: O(n) where n === the length of the longer array
# Space complexity: O(n) where n === the length of the longer array
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1 = {el for el in nums1}
        result = set()

        for el in nums2:
            if el in s1:
                result.add(el)
        return list(result)


# Add other approaches, including sorting and Two Pointers and sorting and Binary Search
