# https://leetcode.com/problems/contains-duplicate/

# Given an integer array nums,
# return true if any value appears at least twice in the array, and return false if every element is distinct.

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        for num in nums:
            if num in num_set:
                return True
            num_set.add(num)
        return False
        # return len(nums) != len(set(nums))


solution = Solution()
nums_list: List[int] = [1, 2, 3, 1]
result = solution.containsDuplicate(nums_list)
print(result)
