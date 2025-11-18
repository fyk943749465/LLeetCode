from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = cnt = 2
        for j in range(2, len(nums)):
            if nums[j - 2] + nums[j - 1] == nums[j]:
                cnt += 1
            else:
                cnt = 2
            ans = max(ans, cnt)
        return ans