from collections import defaultdict
from typing import List


class Solution:
    def minArrivalsToDiscard(self, arrivals: List[int], w: int, m: int) -> int:

        ans = 0
        goodsMap = {}
        isThrowing = [False] * len(arrivals)
        for i, v in enumerate(arrivals):
            if v in goodsMap:
                goodsMap[v] += 1
            else:
                goodsMap[v] = 1

            if (goodsMap[v] > m):
                ans += 1                # 扔物品的计数+1
                isThrowing[i] = True    # 扔掉当前这个物品
                goodsMap[v] = m
            # 离开窗口的元素，需要更新其计数
            if i - w + 1 >= 0 and isThrowing[i - w + 1] == False:
                goodsMap[arrivals[i - w + 1]] -= 1
        return ans

if __name__ == '__main__':
    sol = Solution()
    x = sol.minArrivalsToDiscard([1,2,3,3,3,4], 3, 2)
    print(x)