# Given 2 strings s and t, return true if t is an anagram of s, and false otherwise.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # O(n log n)
        # return sorted(s) == sorted(t)

        # O(n) solutions below
        # counter = [0] * 26
        # for char in s:
        #     counter[ord(char) - ord('a')] += 1
        # for char in t:
        #     counter[ord(char) - ord('a')] -= 1
        #     if counter[ord(char) - ord('a')] < 0:
        #         return False
        # return True

        # using python collections
        # return Counter(s) == Counter(t)


# s = "anagram"
# t = "nagaram"
s = "rat"
t = "car"

solution = Solution()
response = solution.isAnagram(s, t)
print(response)

