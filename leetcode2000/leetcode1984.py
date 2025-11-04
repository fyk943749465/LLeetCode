from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:

        nums.sort()
        ans = 9999999
        for i, c in enumerate(nums):
            if i - k + 1 >= 0:
                ans = min(ans, nums[i] - nums[i - k + 1])
        return ans