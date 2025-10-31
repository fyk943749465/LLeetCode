from typing import List


class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:

        noMProfit = 0
        noFixProfit = 0
        preProfit = [0] * len(strategy)
        lastProfit = [0] * len(strategy)
        preFixProfit = [0] * len(strategy)
        for i, c in enumerate(strategy):
            noMProfit += c * prices[i]
            preProfit[i] = noMProfit
            noFixProfit +=  prices[i]
            preFixProfit[i] = noFixProfit

        for i, c in enumerate(prices):
            lastProfit[i] = noMProfit - preProfit[i]

        ans = noMProfit
        for i, c in enumerate(strategy):
            if i - k + 1 >= 0:
                start = i - k + 1
                mid = (start+i+1)//2
                # 要修改的这一段的值
                if mid > 0:
                    modfiyProfit = preFixProfit[i] - preFixProfit[mid-1]

                preP = 0
                if start > 0:
                    preP = preProfit[start-1]
                ans = max(ans, preP + modfiyProfit + lastProfit[i])
        return ans

if __name__ == '__main__':
    sol = Solution()
    x = sol.maxProfit([9,2,9,5], [-1,0,1,1], 4)
    print(x)