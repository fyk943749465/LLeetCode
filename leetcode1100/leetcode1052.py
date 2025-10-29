from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        ans = 0
        s = 0
        for i, v in enumerate(customers):
            if grumpy[i] == 0:
                s += v
        t = 0
        for i, v in enumerate(grumpy):
            if v == 1:
                t += customers[i]
            if i - minutes + 1 >= 0:
                ans = max(ans, t + s)
                if grumpy[i - minutes + 1] == 1:
                    t -= customers[i - minutes + 1]
        return ans

if __name__ == '__main__':
    solution = Solution()
    x = solution.maxSatisfied([1,0,1,2,1,1,7,5], [0,1,0,1,0,1,0,1], 3)
    print(x)