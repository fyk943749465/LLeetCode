from os import pread
from typing import List


class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:

        s = 0
        maxTime = 0
        for i , v in enumerate(startTime):
            s += endTime[i] - v
            if i - k + 1 >= 0:
                pre = 0
                if i-k + 1 != 0:
                    pre = endTime[i-k]
                if i == len(startTime) - 1:
                    end = eventTime
                else:
                    end = startTime[i+1]
                maxTime = max(maxTime, end - pre - s)
                s -= endTime[i-k+1] - startTime[i-k+1]
        return maxTime

if __name__ == '__main__':
    sol = Solution()
    x = sol.maxFreeTime(5, 1, [1, 3], [2, 5])
    print(x)
