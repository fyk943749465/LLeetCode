from typing import List


class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:

        ans = left = 0
        nums.sort()
        for i, n in enumerate(nums):
            while n - nums[left] > 2 * k:
                left += 1
            ans = max(ans, i - left + 1)
        return ans

