# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_value = float('inf')
        max_gain = 0

        for price in prices:
            if price < min_value:
                min_value = price
            else:
                max_gain = max(max_gain, price - min_value)

        return max_gain


if __name__ == "__main__":
    s = Solution()

    prices = [7, 1, 5, 3, 6, 4]
    print(s.maxProfit(prices))

    prices = [7,6,4,3,1]
    print(s.maxProfit(prices))
