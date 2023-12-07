# https://leetcode.com/problems/longest-consecutive-sequence

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert your array to a set for fast lookup.
        nums_set = set(nums)

        # Initialize the longest streak of delicious burgers
        longest_streak = 0

        for num in nums_set:
            # If this is the start of a potential streak (previous burger is not in the set)
            if num - 1 not in nums_set:
                current_num = num
                current_streak = 1

                # Keep checking for the next burger in the sequence
                while current_num + 1 in nums_set:
                    current_num += 1
                    current_streak += 1

                # Update our longest streak if this 1 is more delicious!
                longest_streak = max(longest_streak, current_streak)

        # Return the height of the mightiest burger tower!
        return longest_streak


if __name__ == "__main__":
    s = Solution()

    nums = [100, 4, 200, 1, 3, 2]
    print(s.longestConsecutive(nums))
