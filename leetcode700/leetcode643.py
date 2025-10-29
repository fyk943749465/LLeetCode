from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        avg = -1e4
        sum = 0
        for i, v in enumerate(nums):
            sum += v
            if i + 1 -k >=0:
                avg = max(avg, sum/k)
                sum -= nums[i+1-k]
        return avg


if __name__ == '__main__':
    s = Solution()
    x = s.findMaxAverage([5], 1)
    print(x)