from typing import List


class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:

        ans = cnt = 0
        for i, v in enumerate(prices):
            if i > 0 and prices[i - 1] - 1 == prices[i]:
                cnt += 1
            else:
                cnt = 1
            ans += cnt
        return ans

