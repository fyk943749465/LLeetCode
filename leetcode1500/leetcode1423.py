from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        ans = 0
        si = len(cardPoints) - k
        for i in range(si, len(cardPoints) + 1):
            if i == si:
                s = sum(cardPoints[i:])
            else:
                s += cardPoints[(i+k-1)%len(cardPoints)]
            ans = max(ans, s)
            # 离开窗口时，更新
            s -= cardPoints[i%len(cardPoints)]
        return ans

if __name__ == '__main__':
    sol = Solution()
    x = sol.maxScore([1,2,3,4,5,6,1], 3)
    print(x)


