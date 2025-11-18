from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:

        i = 0
        ans = 0
        for j, v in enumerate(nums):
            if nums[i] != nums[j]:
                i = j
            if nums[i] == 0:
                ans += (j-i+1)
        return ans