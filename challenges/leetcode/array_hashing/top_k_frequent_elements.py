# https://leetcode.com/problems/top-k-frequent-elements/
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # method using counter
        # counts = Counter(nums)
        # sorted_elements = sorted(counts.keys(), key=lambda x: counts[x], reverse=True)
        # return sorted_elements[:k]

        # method using dict
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1

        # count = dict(sorted(count.items(), key=lambda item: item[1], reverse=True)) # tupla key and value
        final_list = sorted(count.keys(), key=lambda item: count[item], reverse=True)

        return final_list[:2]


if __name__ == "__main__":
    s = Solution()

    nums: List[int] = [1, 1, 1, 2, 2, 3]
    k: int = 2

    response = s.topKFrequent(nums, k)
    print(response)
