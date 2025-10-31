from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:

        k = 0
        for i, c in enumerate(nums):
            if c == 1:
                k += 1

        if k == 0:
            return 0
        minZeroCnt = len(nums) - k
        zeroCnt = 0
        for i in  range(2 * len(nums)):
            if nums[i%len(nums)] == 0:
                zeroCnt += 1
            # 窗口大小为k
            if i - k + 1 >= 0:
                minZeroCnt = min(minZeroCnt, zeroCnt)
                if minZeroCnt == 0:
                    break
                # 出窗口后，减去计数
                if nums[(i-k+1)%(len(nums))] == 0:
                    zeroCnt -= 1
        return minZeroCnt